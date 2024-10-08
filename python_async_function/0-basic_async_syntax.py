#!/usr/bin/env python3
"""Waits for random"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

