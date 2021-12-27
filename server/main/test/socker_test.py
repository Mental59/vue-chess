# import socket

# sock = socket.socket()
# sock.connect(("0.0.0.0", 6543))

# sock.send("CREATE ROOM".encode("utf-8"))

import websockets
import asyncio


async def hello():
    async with websockets.connect("ws://0.0.0.0:5001") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()

asyncio.run(hello())
