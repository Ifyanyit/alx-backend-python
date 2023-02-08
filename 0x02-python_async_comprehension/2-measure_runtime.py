#!/usr/bin/env python3
'''Task 0 - Async Generator'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather, it then measures the total runtime and returns it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
