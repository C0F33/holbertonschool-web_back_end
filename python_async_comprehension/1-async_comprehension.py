#!/usr/bin/env python3
"""async function"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async_comprehension """
    return [n async for n in async_generator()]