#!/usr/bin/env python3
''' type-annotated function element_longth'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    args:
        lst: iterable
    returns:
        list
    '''
    return [(i, len(i)) for i in ls]
