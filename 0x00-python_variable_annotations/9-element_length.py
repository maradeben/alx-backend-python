#!/usr/bin/env python3
""" typing an iterable object """
from typing import List, Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ typing iterable """
    return [(i, len(i)) for i in list]
