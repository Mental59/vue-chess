# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import matchmaker_pb2 as matchmaker__pb2


class MatchmakerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetGameList = channel.unary_stream(
        '/matchmaker.Matchmaker/GetGameList',
        request_serializer=matchmaker__pb2.User.SerializeToString,
        response_deserializer=matchmaker__pb2.Game.FromString,
        )
    self.CreateGame = channel.unary_unary(
        '/matchmaker.Matchmaker/CreateGame',
        request_serializer=matchmaker__pb2.User.SerializeToString,
        response_deserializer=matchmaker__pb2.Game.FromString,
        )
    self.CloseGame = channel.unary_unary(
        '/matchmaker.Matchmaker/CloseGame',
        request_serializer=matchmaker__pb2.Game.SerializeToString,
        response_deserializer=matchmaker__pb2.Status.FromString,
        )
    self.JoinPlayer = channel.unary_unary(
        '/matchmaker.Matchmaker/JoinPlayer',
        request_serializer=matchmaker__pb2.JoinRequest.SerializeToString,
        response_deserializer=matchmaker__pb2.Status.FromString,
        )
    self.JoinVisitor = channel.unary_unary(
        '/matchmaker.Matchmaker/JoinVisitor',
        request_serializer=matchmaker__pb2.JoinRequest.SerializeToString,
        response_deserializer=matchmaker__pb2.Status.FromString,
        )


class MatchmakerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetGameList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateGame(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseGame(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JoinPlayer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JoinVisitor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MatchmakerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetGameList': grpc.unary_stream_rpc_method_handler(
          servicer.GetGameList,
          request_deserializer=matchmaker__pb2.User.FromString,
          response_serializer=matchmaker__pb2.Game.SerializeToString,
      ),
      'CreateGame': grpc.unary_unary_rpc_method_handler(
          servicer.CreateGame,
          request_deserializer=matchmaker__pb2.User.FromString,
          response_serializer=matchmaker__pb2.Game.SerializeToString,
      ),
      'CloseGame': grpc.unary_unary_rpc_method_handler(
          servicer.CloseGame,
          request_deserializer=matchmaker__pb2.Game.FromString,
          response_serializer=matchmaker__pb2.Status.SerializeToString,
      ),
      'JoinPlayer': grpc.unary_unary_rpc_method_handler(
          servicer.JoinPlayer,
          request_deserializer=matchmaker__pb2.JoinRequest.FromString,
          response_serializer=matchmaker__pb2.Status.SerializeToString,
      ),
      'JoinVisitor': grpc.unary_unary_rpc_method_handler(
          servicer.JoinVisitor,
          request_deserializer=matchmaker__pb2.JoinRequest.FromString,
          response_serializer=matchmaker__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'matchmaker.Matchmaker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))