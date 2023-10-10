#!/usr/bin/env python3
""" basic async syntax with random delay """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ simple async function """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
