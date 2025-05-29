import threading, time

def task(name):
    print(f"Задача {name} началась\n")
    time.sleep(2)
    print(f"\nЗадача {name} завершена")

for i in range(5):
    t = threading.Thread(target=task, args=(f"Поток {i+1}",))
    t.start()

import asyncio

async def async_task(name):
    print(f"Асинхронная задача {name} началась")
    await asyncio.sleep(2)
    print(f"Асинхронная задача {name} завершена")

tasks = [asyncio.create_task(async_task(f"Задача {i+1}")) for i in range(5)]

async def main():
    await asyncio.gather(*(async_task(f"Задача {i+1}") for i in range(5)))
    await main()