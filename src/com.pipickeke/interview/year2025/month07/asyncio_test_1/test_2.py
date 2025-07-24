import asyncio


async def long_operation():
    await asyncio.sleep(10)
    return "Done"

async def main():
    try:
        #
        result = await asyncio.wait_for(long_operation(), timeout=2)
        print("wait...")
    except asyncio.TimeoutError as e:
        print("Timeout")

asyncio.run(main())
