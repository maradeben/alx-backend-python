#!/usr/bin/env python3
""" basic async syntax with random delay """
import asyncio
import random


async def wait_random(max_delay=10):
    """ simple async function """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
