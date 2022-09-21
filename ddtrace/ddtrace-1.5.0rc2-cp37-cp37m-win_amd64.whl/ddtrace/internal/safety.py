from typing import Any
from typing import Iterator
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import Union

from ddtrace.internal.compat import BUILTIN
from ddtrace.internal.compat import PY3
from ddtrace.internal.utils.attrdict import AttrDict
from ddtrace.internal.utils.cache import cached
from ddtrace.vendor import wrapt


NoneType = type(None)

if PY3:
    long = int


def _maybe_slots(obj):
    # type: (Any) -> Union[Tuple[str], List[str]]
    try:
        slots = object.__getattribute__(obj, "__slots__")
        if isinstance(slots, str):
            return (slots,)
        return slots
    except AttributeError:
        return []


@cached()
def _slots(_type):
    # type: (Type) -> Set[str]
    return {_ for cls in object.__getattribute__(_type, "__mro__") for _ in _maybe_slots(cls)}


def get_slots(obj):
    # type: (Any) -> Set[str]
    """Get the object's slots."""
    return _slots(type(obj))


def _isinstance(obj, types):
    # type: (Any, Union[Type, Tuple[Union[Type, Tuple[Any, ...]], ...]]) -> bool
    # DEV: isinstance falls back to calling __getattribute__ which could cause
    # side effects.
    return issubclass(type(obj), types)


class SafeObjectProxy(wrapt.ObjectProxy):
    """Object proxy to make sure we don't call unsafe code.

    Access to the wrapped object is denied to prevent any potential
    side-effects. Arbitrary objects are essentially converted into attribute
    dictionaries. Callable objects are made uncallable to prevent accidental
    calls that can also trigger side-effects.
    """

    def __call__(self, *args, **kwargs):
        # type: (Any, Any) -> Optional[Any]
        raise RuntimeError("Cannot call safe object")

    def __getattribute__(self, name):
        # type: (str) -> Any
        if name == "__wrapped__":
            raise AttributeError("Access denied")

        return super(SafeObjectProxy, self).__getattribute__(name)

    def __getattr__(self, name):
        # type: (str) -> Any
        return type(self).safe(super(SafeObjectProxy, self).__getattr__(name))

    def __getitem__(self, item):
        # type: (Any) -> Any
        return type(self).safe(super(SafeObjectProxy, self).__getitem__(item))

    def __iter__(self):
        # type: () -> Any
        return iter(type(self).safe(_) for _ in super(SafeObjectProxy, self).__iter__())

    def items(self):
        # type: () -> Iterator[Tuple[Any, Any]]
        return (
            (type(self).safe(k), type(self).safe(v)) for k, v in super(SafeObjectProxy, self).__getattr__("items")()
        )

    # Custom object representations might cause side-effects
    def __str__(self):
        return object.__repr__(self)

    __repr__ = __str__

    @classmethod
    def safe(cls, obj):
        # type: (Any) -> Optional[Any]
        """Turn an object into a safe proxy."""
        _type = type(obj)

        if _isinstance(obj, type):
            try:
                if obj.__module__ == BUILTIN:
                    # We are assuming that builtin types are safe
                    return obj
            except AttributeError:
                # No __module__ attribute. We'll use caution
                pass

        elif _type in {str, int, float, bool, NoneType, bytes, complex, long}:
            # We are assuming that scalar builtin type instances are safe
            return obj

        try:
            return cls(AttrDict(object.__getattribute__(obj, "__dict__")))
        except AttributeError:
            pass

        slots = get_slots(obj)
        if slots:
            # Handle slots objects
            return cls(AttrDict({k: object.__getattribute__(obj, k) for k in slots}))

        # raise TypeError("Unhandled object type: %s", type(obj))
        return cls(obj)
