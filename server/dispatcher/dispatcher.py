import asyncio
import pickle
from typing import AsyncIterable, Iterable
import aioredis
import grpc
import json
import socket

import dispatcher_pb2 as disp
import dispatcher_pb2_grpc as disp_grpc
import setting as s
import status_message as msg


redis = None

serversList = s.SERVER_LIST
cur_server = 0


def create_room():
    global cur_server
    index = cur_server
    sock = socket.socket()
    for i in range(0, len(serversList)):
        try:
            sock.connect((serversList[index]['host'], serversList[index]['port']))
            break
        except Exception as e:
            print(str(e))
            index = (index+1) % len(serversList)
    cur_server = (index+1) % len(serversList)
    sock.send('CREATE ROOM'.encode('utf-8'))
    data = sock.recv(1024)
    sock.close()

    return(json.loads(data.decode("utf-8")))


class DispatcherServicer(disp_grpc.DispatcherServicer):
    def __init__(self) -> None:
        pass

    async def GetGameList(self, request: disp.User,
                          unused_context) -> AsyncIterable[disp.Game]:
        print("Start GetGameList")
        async for key in redis.scan_iter("*"):
            print(f"key {key}")
            pgame = await redis.get(key)
            game = pickle.loads(pgame)
            print(game)
            yield game

    async def CreateGame(self, request: disp.User,
                         unused_context) -> disp.Game:
        # {host,port} возвращает словарь с host port
        json_game = create_room()
        game = disp.Game(owner=request, state=0,
                         address=json_game["host"], port=json_game["port"])
        pgame = pickle.dumps(game)

        async with redis.client() as conn:
            await conn.set(request.uuid, pgame)
        return game

    async def CloseGame(self, request: disp.Game,
                        unused_context) -> disp.Status:
        async with redis.client() as conn:
            pgame = pickle.dumps(request)
            await conn.set(request.uuid, pgame)

    async def JoinPlayer(self, request: disp.JoinRequest,
                         unused_context) -> disp.Status:
        async with redis.client() as conn:
            game = await conn.get(request.user.uuid)
            if game is not None:
                status = disp.Status(400, msg.STATUS[400])
            else:
                # TODO: Add code
                status = disp.Status(500, msg.STATUS[500])

    async def JoinVisitor(self, request: disp.Game,
                          context) -> disp.Status:
        async with redis.client() as conn:
            game = await conn.get(request.user.uuid)
            if game is not None:
                # TODO: Add code
                status = disp.Status(400, msg.STATUS[400])
            else:
                status = disp.Status(500, msg.STATUS[500])


async def serve() -> None:
    server = grpc.aio.server()
    disp_grpc.add_DispatcherServicer_to_server(DispatcherServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    redis = aioredis.from_url(s.REDIS_SERVER, encoding="utf-8", decode_responses=True)
    asyncio.run(serve())
