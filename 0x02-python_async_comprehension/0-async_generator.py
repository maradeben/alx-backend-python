#!/usr/bin/env pythn3
""" make an asynchronous generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, float]:
    """ yield 10 random numbers async """

    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
