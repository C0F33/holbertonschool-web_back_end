#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""Coroutines"""
async def wait_n(n: int, max_delay: int):
    """COroutines"""
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]

