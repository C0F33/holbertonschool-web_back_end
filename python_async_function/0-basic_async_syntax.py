#!/usr/bin/python3
import asyncio
import random
"""Waits for random"""
async def wait_random(max_delay: int = 10) -> float:
    """Randomfunc"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if (__name__ == "__main__"):
    wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
