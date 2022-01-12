import asyncio
import logging
import pickle
from typing import AsyncIterable, Iterable
import redis as credis
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

    return json.loads(data.decode("utf-8")), serversList[index]['host']


class DispatcherServicer(disp_grpc.DispatcherServicer):
    def __init__(self) -> None:
        pass

    async def GetGameList(self, request: disp.User,
                          unused_context) -> AsyncIterable[disp.Game]:
        # logging.info(f"User {request.uuid} user requested a list of games")
        for key in redis.scan_iter("*"):
            pgame = redis.get(key)
            game = pickle.loads(pgame)
            yield game

    async def CreateGame(self, request: disp.User,
                         unused_context) -> disp.Game:
        json_game, host  = create_room()
        game = disp.Game(owner=request, state=0,
                         address=host, port=json_game["port"])
        pgame = pickle.dumps(game)
        with redis.client() as conn:
            conn.set(request.uuid, pgame)

        logging.info(f"User {request.uuid} is trying to create games")

        return game

    async def CloseGame(self, request: disp.Game,
                        unused_context) -> disp.Status:
        with redis.client() as conn:
            game = conn.get(request.owner.uuid)
            if game is not None:
                game = request
                game.state = 2
                pgame = pickle.dumps(game)
                conn.set(request.owner.uuid, pgame)
                conn.expire(request.owner.uuid, s.ROOM_DELETE_TIMEOUT)
                status = disp.Status(code=200, text=msg.STATUS[200])
            else:
                status = disp.Status(code=500, text=msg.STATUS[500])

        logging.info(f"Game {request.owner.uuid} was closed. It deletes after {s.ROOM_DELETE_TIMEOUT} second.")

        return status

    async def JoinPlayer(self, request: disp.JoinRequest,
                         unused_context) -> disp.Status:
        with redis.client() as conn:
            game = conn.get(request.user.uuid)
            if game is not None:
                game = request.game
                game.state = 1
                pgame = pickle.dumps(game)
                conn.set(request.game.owner.uuid, pgame)
                # Success
                status = disp.Status(code=200, text=msg.STATUS[200])
            else:
                # There is no selected room
                status = disp.Status(code=500, text=msg.STATUS[500])

        logging.info(f"The player {request.user.uuid} has joined the room.")

        return status

    async def JoinVisitor(self, request: disp.JoinRequest,
                          context) -> disp.Status:
        with redis.client() as conn:
            game = conn.get(request.game.owner.uuid)
            if game is not None:
                status = disp.Status(code=200, text=msg.STATUS[200])
            else:
                status = disp.Status(code=500, text=msg.STATUS[500])

        logging.info(f"The viewer {request.user.uuid} has joined the room {request.game.owner.uuid}.")

        return status


async def serve() -> None:
    server = grpc.aio.server()
    disp_grpc.add_DispatcherServicer_to_server(DispatcherServicer(), server)
    server.add_insecure_port('0.0.0.0:14586')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
        datefmt='%H:%M:%S',
    )
    redis = credis.from_url(s.REDIS_SERVER, encoding="utf-8", decode_responses=False)
    asyncio.run(serve())
