# -- coding: utf-8 --
import asyncio

async def start_strongman(name, power):

    number = 0
    print(f'Силач {name} начал соревнования')
    for _ in range(5):
        number += 1
        await asyncio.sleep(6 - power)
        print(f'Силач {name} поднял {number} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():

    first = asyncio.create_task(start_strongman('Pasha', 3))
    second = asyncio.create_task(start_strongman('Denis', 4))
    third = asyncio.create_task(start_strongman('Apollon', 5))
    await first
    await second
    await third


asyncio.run(start_tournament())