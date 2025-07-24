import asyncio


async def task():
    print("coroutine")



async def main():
    await task()


asyncio.run(main())
