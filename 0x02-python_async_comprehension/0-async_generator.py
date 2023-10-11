#!/usr/bin/env pythn3
""" make an asynchronous generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ yield 10 random numbers async """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
