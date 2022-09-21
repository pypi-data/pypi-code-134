from threading import RLock
from typing import Any
from typing import Callable
from typing import Optional
from typing import Type
from typing import TypeVar


miss = object()

T = TypeVar("T")
S = TypeVar("S")
F = Callable[[T], S]
M = Callable[[Any, T], S]


class LFUCache(dict):
    """Simple LFU cache implementation.

    This cache is designed for memoizing functions with a single hashable
    argument. The eviction policy is LFU, i.e. the least frequently used values
    are evicted when the cache is full. The amortized cost of shrinking the
    cache when it grows beyond the requested size is O(log(size)).
    """

    def __init__(self, maxsize=256):
        # type: (int) -> None
        self.maxsize = maxsize
        self.lock = RLock()

    def get(self, key, f):  # type: ignore[override]
        # type: (T, F) -> S
        """Get a value from the cache.

        If the value with the given key is not in the cache, the expensive
        function ``f`` is called on the key to generate it. The return value is
        then stored in the cache and returned to the caller.
        """
        if len(self) >= self.maxsize:
            for _, h in zip(range(self.maxsize >> 1), sorted(self, key=lambda h: self[h][1])):
                del self[h]

        _ = super(LFUCache, self).get(key, miss)
        if _ is not miss:
            value, count = _
            self[key] = (value, count + 1)
            return value

        with self.lock:
            _ = super(LFUCache, self).get(key, miss)
            if _ is not miss:
                value, count = _
                self[key] = (value, count + 1)
                return value

            value = f(key)

            self[key] = (value, 1)

            return value


def cached(maxsize=256):
    # type: (int) -> Callable[[F], F]
    """Decorator for memoizing functions of a single argument (LFU policy)."""

    def cached_wrapper(f):
        # type: (F) -> F
        cache = LFUCache(maxsize)

        def cached_f(key):
            # type: (T) -> S
            return cache.get(key, f)

        cached_f.invalidate = cache.clear  # type: ignore[attr-defined]

        return cached_f

    return cached_wrapper


class CachedMethodDescriptor(object):
    def __init__(self, method, maxsize):
        # type: (M, int) -> None
        self._method = method
        self._maxsize = maxsize

    def __get__(self, obj, objtype=None):
        # type: (Any, Optional[Type]) -> F
        cached_method = cached(self._maxsize)(self._method.__get__(obj, objtype))
        setattr(obj, self._method.__name__, cached_method)
        return cached_method


def cachedmethod(maxsize=256):
    # type: (int) -> Callable[[M], CachedMethodDescriptor]
    """Decorator for memoizing methods of a single argument (LFU policy)."""

    def cached_wrapper(f):
        # type: (M) -> CachedMethodDescriptor
        return CachedMethodDescriptor(f, maxsize)

    return cached_wrapper
