#!/usr/bin/env python3
"""generates random numbers between 1 and 10 waiting time in seconds between 1 and 10"""
import asyncio
import random
from typing import Generator
async def async_generator() -> Generator[float, None, None]:
"""async function"""
    for i in range(11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)