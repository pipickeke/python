"""

协程 coroutine 测试

"""
import asyncio

async def fetch_data(url: str):
    print(f"fetch {url}...")
    await asyncio.sleep(2)
    return f"data from {url}.."



async def main():
    # 创建3个并发任务
    task1 = asyncio.create_task(fetch_data("http://example-1"))
    task2 = asyncio.create_task(fetch_data("http://example-2"))
    task3 = asyncio.create_task(fetch_data("http://example-3"))

    # 等待所有任务完成
    result = await asyncio.gather(task1, task2, task3)
    print(f"Result: {result}")

asyncio.run(main())