#!/usr/bin/env python3
""" run async comprehension and measure runtime """
import asyncio
import typing
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ gather and execute async_comprehension """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    return (time.time() - start)
