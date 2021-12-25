import asyncio
import logging
import random
from typing import AsyncIterable, Iterable


import grpc
import grpc.matchmaker_pb2 as mm
import grpc.matchmaker_pb2_grpc as mm_grpc


class MatchmakerServicer(mm_grpc.MatchmakerServicer):
    def __init__(self) -> None:
        pass

    async def GetGameList(self, request: mm.User,
                          unused_context) -> AsyncIterable[mm.Game]:
        pass

    async def CreateGame(self, request: mm.User,
                         unused_context) -> mm.Game:
        pass

    async def CloseGame(self, request: mm.Game,
                        unused_context) -> mm.Status:
        pass

    async def JoinPlayer(self, request: mm.JoinRequest,
                         unused_context) -> mm.Game:
        pass

    async def JoinVisitor(self, request: mm.Game,
                          context) -> mm.Game:
        pass


async def serve() -> None:
    server = grpc.aio.server()
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())