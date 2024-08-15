#!/usr/bin/env python3
from time import time as current_time
from asyncio import run
"""Module"""
wait_n = __import__ ("1-concurrent_coroutines").wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Try this"""
    start_time = current_time()

    run(wait_n(n, max_delay))

    end_time = current_time()

    total_time = end_time - start_time
    return total_time / n
