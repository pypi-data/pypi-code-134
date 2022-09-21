import json
from typing import TYPE_CHECKING, Optional, Type

from pydantic import ConstrainedFloat, ConstrainedInt, ConstrainedStr

from ..validators import sanitize_dict, sanitize_item, validate_digits

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class SantizedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sanitize_dict(self)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        return sanitize_item(o, default=super().default)


class StrictPositiveInt(ConstrainedInt):
    """
    - strict: ensures a float isn't passed in by accident
    - ge (greater than or equal): ensures the value is above 0
    """

    strict = True
    ge = 0
    le = 21_474_836_47  # Max value in DB

    ...


class StrictPositiveFloat(ConstrainedFloat):
    """
    - strict: ensures an integer isn't passed in by accident
    - ge (greater than or equal): ensures the value is above 0
    """

    strict = True
    ge = 0

    ...


def digits(
    min_length: Optional[int] = None, max_length: Optional[int] = None
) -> Type[str]:
    namespace = dict(min_length=min_length, max_length=max_length)
    return type('DigitsValue', (Digits,), namespace)


class Digits(ConstrainedStr):
    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield from ConstrainedStr.__get_validators__()
        yield validate_digits
