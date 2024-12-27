import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.'")
    balls = 5
    for ball in range(balls):
        await asyncio.sleep(1/power)
        print(f"Силач {name} поднял {ball+1} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Pasha",3))
    task2 = asyncio.create_task(start_strongman("Denis",4))
    task3 = asyncio.create_task(start_strongman("Appolon",5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

