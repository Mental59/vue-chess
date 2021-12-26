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

serversList=[]
serversList.append({"host":"localhost", "port":6543}) #Просто добавляю сервер в список доступных серверов
cur_server=0

def CreateRoom():
    global cur_server
    index=cur_server
    sock = socket.socket()
    for i in range(0,len(serversList)):
        try:
            sock.connect((serversList[index]['host'],serversList[index]['port']))
            break
        except:
            index+=1
            index=divmod(index, len(serversList))
    cur_server=divmod(index+1, len(serversList))
    sock.send('CREATE ROOM'.encode('utf-8'))

    data = sock.recv(1024)
    sock.close()
    return(json.loads(data.decode("utf-8")))


class DispatcherServicer(disp_grpc.DispatcherServicer):
    def __init__(self) -> None:
        pass

    async def GetGameList(self, request: disp.User,
                          unused_context) -> AsyncIterable[disp.Game]:
        async for key in redis.scan_iter("*"):
            pgame = await redis.get(key)
            game = pickle.loads(pgame)
            yield game
        pass

    async def CreateGame(self, request: disp.User,
                         unused_context) -> disp.Game:
        game = disp.Game(owner=request, state=0,
                         address="0.0.0.0", port="8080")
        pgame = pickle.dumps(game)
        jsonGame=CreateGame() # {host,port} возвращает словарь с host port
        async with redis.client() as conn:
            await conn.set(request.uuid, pgame)
        return game

    async def CloseGame(self, request: disp.Game,
                        unused_context) -> disp.Status:
        async with redis.client() as conn:
            await conn.set(request.uuid, pgame)

    async def JoinPlayer(self, request: disp.JoinRequest,
                         unused_context) -> disp.Status:
        async with redis.client() as conn:
            game = await conn.get(gane.user.uuid)
            if game is not None:
                status = disp.Status(400, msg.STATUS[400])
            else:
                # TODO: Add code
                status = disp.Status(500, msg.STATUS[500])

    async def JoinVisitor(self, request: disp.Game,
                          context) -> disp.Status:
        async with redis.client() as conn:
            game = await conn.get(game.user.uuid)
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
    asyncio.get_event_loop().run_until_complete(serve())
