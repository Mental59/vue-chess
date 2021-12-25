import grpc
import matchmaker_pb2
import matchmaker_pb2_grpc

from concurrent.futures import ThreadPoolExecutor


class MatchmakerService(matchmaker_pb2_grpc.MatchmakerServicer):
    def __init__(self) -> None:
        super().__init__()
    
    def JoinPlayer(self, request, context):
        print(' [INFO] Received message!')
        print(f' [INFO] Request: {request}', f'Context: {context}', sep='\n')
        return matchmaker_pb2.Status(code=123)


def main():
    server = grpc.server(ThreadPoolExecutor(max_workers=8))
    matchmaker_pb2_grpc.add_MatchmakerServicer_to_server(MatchmakerService(), server)
    server.add_insecure_port('[::]:14586')
    server.start()
    print(' [INFO] Server started')
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted!')
