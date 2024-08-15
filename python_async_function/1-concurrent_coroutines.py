#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""Coroutines"""
async def wait_n(n: int, max_delay: int):
    """COroutines"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)];
    results = await asyncio.gather(*tasks)

    delays.extend(results)
    return sorted(delays)
