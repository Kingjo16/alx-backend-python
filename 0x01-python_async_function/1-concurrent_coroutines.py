#!/usr/bin/env python3
'''Module for Task 1: Execute wait_random multiple times.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(num_times: int, max_delay: int) -> List[float]:
    '''Executes wait_random num_times times and returns the list.'''
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(num_times)))
    )
    return sorted(delay_times)
