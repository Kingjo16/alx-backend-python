#!/usr/bin/env python3
'''Module for Task 0: Wait for a random delay.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random amount of time up to max_delay seconds.'''
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
