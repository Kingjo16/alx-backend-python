#!/usr/bin/env python3
'''Task 0x02-python_async_comph module.'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creat a 10-Number generator python_async_comp.'''
    return [num async for num in async_generator()]
