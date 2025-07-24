
"""

生产者消费者测试

"""
import asyncio


async def producer(queue: asyncio.Queue, count: int):
    for i in range(count):
        await queue.put(i)
        print(f"Producer: {i}")
        await asyncio.sleep(0.1) #控制生产速度

async def consumer(quue: asyncio.Queue, name: str):
    while True:
        item = await quue.get()
        print(f"Consumer {name} get: {item}")
        await asyncio.sleep(0.5)
        quue.task_done()

async def main():
    queue = asyncio.Queue()

    #
    producer_task = asyncio.create_task(producer(queue, 5))
    consumers = [
        asyncio.create_task(consumer(queue, 'A')),
        asyncio.create_task(consumer(queue, 'B'))
    ]
    await producer_task
    await queue.join() # 等待队列处理完毕
    for c in consumers:
        c.cancel()

asyncio.run(main())






