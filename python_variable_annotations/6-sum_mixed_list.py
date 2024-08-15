#!/usr/bin/env python3
"""this function takes  two paramteres and converts them to a mixed list of ints and floats"""

from typing import Union, List

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sum_mixed_list"""
    return sum(mxd_list)