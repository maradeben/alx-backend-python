#!/usr/bin/env python3
""" typed string and int/float, put into tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return key and squared value """
    return ((k, float(v**2)))
