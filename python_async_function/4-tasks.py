#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
"""Coroutines are interesting"""
async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """COroutines really are"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
