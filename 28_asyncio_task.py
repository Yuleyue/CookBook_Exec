#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/5 19:24
Email : adamyue@163.com
'''

import asyncio
import time


async def call_api(name:str, delay:float):
    print(f'{name} - step 1')
    await asyncio.sleep(delay)          # simulate a status like io operation
    print(f'{name} - step 2')
async def main():
    time_start = time.perf_counter()
    print('Begin A coroutine')
    task_1 = asyncio.create_task(call_api('A', 3))

    print('Begin B coroutine')
    task_2 = asyncio.create_task(call_api('B', 2))

    await task_1
    print('task_1 completed')
    await task_2
    print('task_2 completed')

    time_end = time.perf_counter()
    print(f'Time taken: {time_end - time_start}')

asyncio.run(main())