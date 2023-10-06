#!/usr/bin/env python3
""" typed mixed list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ add a mixed list """
    return (sum(mxd_list))
