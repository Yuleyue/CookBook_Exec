#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/5 20:22
Email : adamyue@163.com
'''
import asyncio


async def play_music(music: str):
    print(f'Playing music...{music}')
    await asyncio.sleep(5)
    print(f'Music is finished...{music}')
    return music

async def my_cancel():
    task = asyncio.create_task(play_music('A'))
    await asyncio.sleep(3)
    if not task.done():
        task.cancel()

if __name__ == '__main__':
    asyncio.run(my_cancel())
