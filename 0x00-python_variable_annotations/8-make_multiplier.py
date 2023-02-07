#!/usr/bin/env python3
''' type-annotated function sum_mixed_list'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Args:
        multiplier: float
    Return:
        returns a function that multiplies a float by multiplier
    '''
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
