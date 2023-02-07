#!/usr/bin/env python3
''' type-annotated function sum_list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Args:
        input_list: list[float]
    Return:
        float
    '''
    return sum(input_list)
