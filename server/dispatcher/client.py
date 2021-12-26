
import asyncio
import logging
import random
from typing import Iterable, List
import uuid

import grpc
import dispatcher_pb2 as disp
import dispatcher_pb2_grpc as disp_grpc


async def create_game(stub: disp_grpc.DispatcherStub) -> None:
    user = disp.User(uuid="1", name="1")
    game = await stub.CreateGame(user)
    print(game.owner)


async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = disp_grpc.DispatcherStub(channel)
        await create_game(stub)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())