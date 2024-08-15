from time import time as current_time
from asyncio import run
"""Module"""
wait_n = __import__ ("1-concurrent_coroutines").wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Try this"""
    start = current_time()
    run(wait_n(n, max_delay))
    end = current_time()
    total_time = end - start
    return (total_time)
