import asyncio


async def producer(queue: asyncio.Queue, count: int):
    for i in range(count):
        await queue.put(i)
        print(f"producer {i}")
        await asyncio.sleep(1)

async def consumer(queue: asyncio.Queue, name: str):
    while True:
        item = await queue.get()
        print(f"consumer {name} get {item}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue, 5))
    consumers = [
        asyncio.create_task(consumer(queue, 'A')),
        asyncio.create_task(consumer(queue, 'B'))
    ]

    await producer_task
    await queue.join()

    for c in consumers:
        c.cancel()

asyncio.run(main())




