#!/usr/bin/python3
import asyncio
import random
"""Waits for random"""
async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
