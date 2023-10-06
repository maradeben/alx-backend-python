#!/usr/bin/env python3
""" safely get values """
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """ safe values """
    if key in dct:
        return dct[key]
    else:
        return default
