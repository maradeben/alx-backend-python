#!/usr/bin/python3
""" first element of sequence, annotation
    types are not known for sure
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return first element of list """
    if lst:
        return lst[0]
    else:
        return None
