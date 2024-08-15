#!/usr/bin/python3
import asyncio
import random
"""Waits for random"""
async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay"""
    result = random.uniform(0, max_delay)
    await asyncio.sleep(result)

    return result
