import asyncio
import websockets
import threading
import sys




async def hello():
    for x in range(1000):
        async with websockets.connect("ws://localhost:8083") as websocket:
            await websocket.send(str(x))
            name = await websocket.recv()
            print(name,end = ' ', flush=True)
            sys.stdout.flush()


async def main():
    await asyncio.wait([
        hello(),
        hello(),
        hello(),

    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())