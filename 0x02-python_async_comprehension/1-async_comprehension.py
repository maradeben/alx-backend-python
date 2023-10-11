#!/usr/bin/env python3
""" async coroutine """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ call a generator function and collect with comprehension """
    result = [i async for i in async_generator()]

    return result
