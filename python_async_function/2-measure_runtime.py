#!/usr/bin/env python3
from time import time as current_time
from asyncio import run
"""MFrom the previous file, import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay as
    arguments that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.

    Use the time module to measure an approximate elapsed time."""
wait_n = __import__ ("1-concurrent_coroutines").wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Try this"""
    start_time = current_time()

    run(wait_n(n, max_delay))

    end_time = current_time()

    total_time = end_time - start_time
    return total_time / n
