#!/usr/bin/env python3
''' type-annotated function sum_mixed_list'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Args:
        input_list: list[Union[float , int]]
    Return:
        float
    '''
    return (k, float(v**2))
