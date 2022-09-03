import asyncio
from danbotstatus import AsynchronousState

async def main():
    """
    Basic Example for AsynchronousState
    """
    instance = AsynchronousState()
    print(await instance.fetch_all())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
