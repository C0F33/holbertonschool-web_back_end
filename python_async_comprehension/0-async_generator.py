#!/usr/bin/env python3
import asyncio
import random
"""generates random numbers between 1 and 10 waiting time in seconds between 1 and 10"""
async def async_generator():
"""async function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
