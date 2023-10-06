#!/usr/bin/env python3
""" type-annotated function
    takes a float and returns function that multiplies
    a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float
        by the given multiplier
    """

    return (lambda x: x * multiplier) 
