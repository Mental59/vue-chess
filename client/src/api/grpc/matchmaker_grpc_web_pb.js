/**
 * @fileoverview gRPC-Web generated client stub for matchmaker
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.matchmaker = require('./matchmaker_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.matchmaker.MatchmakerClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.matchmaker.MatchmakerPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.matchmaker.User,
 *   !proto.matchmaker.Game>}
 */
const methodDescriptor_Matchmaker_GetGameList = new grpc.web.MethodDescriptor(
  '/matchmaker.Matchmaker/GetGameList',
  grpc.web.MethodType.SERVER_STREAMING,
  proto.matchmaker.User,
  proto.matchmaker.Game,
  /**
   * @param {!proto.matchmaker.User} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.matchmaker.Game.deserializeBinary
);


/**
 * @param {!proto.matchmaker.User} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.matchmaker.Game>}
 *     The XHR Node Readable Stream
 */
proto.matchmaker.MatchmakerClient.prototype.getGameList =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/matchmaker.Matchmaker/GetGameList',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_GetGameList);
};


/**
 * @param {!proto.matchmaker.User} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.matchmaker.Game>}
 *     The XHR Node Readable Stream
 */
proto.matchmaker.MatchmakerPromiseClient.prototype.getGameList =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/matchmaker.Matchmaker/GetGameList',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_GetGameList);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.matchmaker.User,
 *   !proto.matchmaker.Game>}
 */
const methodDescriptor_Matchmaker_CreateGame = new grpc.web.MethodDescriptor(
  '/matchmaker.Matchmaker/CreateGame',
  grpc.web.MethodType.UNARY,
  proto.matchmaker.User,
  proto.matchmaker.Game,
  /**
   * @param {!proto.matchmaker.User} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.matchmaker.Game.deserializeBinary
);


/**
 * @param {!proto.matchmaker.User} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.matchmaker.Game)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.matchmaker.Game>|undefined}
 *     The XHR Node Readable Stream
 */
proto.matchmaker.MatchmakerClient.prototype.createGame =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/matchmaker.Matchmaker/CreateGame',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_CreateGame,
      callback);
};


/**
 * @param {!proto.matchmaker.User} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.matchmaker.Game>}
 *     Promise that resolves to the response
 */
proto.matchmaker.MatchmakerPromiseClient.prototype.createGame =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/matchmaker.Matchmaker/CreateGame',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_CreateGame);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.matchmaker.Game,
 *   !proto.matchmaker.Status>}
 */
const methodDescriptor_Matchmaker_CloseGame = new grpc.web.MethodDescriptor(
  '/matchmaker.Matchmaker/CloseGame',
  grpc.web.MethodType.UNARY,
  proto.matchmaker.Game,
  proto.matchmaker.Status,
  /**
   * @param {!proto.matchmaker.Game} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.matchmaker.Status.deserializeBinary
);


/**
 * @param {!proto.matchmaker.Game} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.matchmaker.Status)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.matchmaker.Status>|undefined}
 *     The XHR Node Readable Stream
 */
proto.matchmaker.MatchmakerClient.prototype.closeGame =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/matchmaker.Matchmaker/CloseGame',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_CloseGame,
      callback);
};


/**
 * @param {!proto.matchmaker.Game} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.matchmaker.Status>}
 *     Promise that resolves to the response
 */
proto.matchmaker.MatchmakerPromiseClient.prototype.closeGame =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/matchmaker.Matchmaker/CloseGame',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_CloseGame);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.matchmaker.JoinRequest,
 *   !proto.matchmaker.Status>}
 */
const methodDescriptor_Matchmaker_JoinPlayer = new grpc.web.MethodDescriptor(
  '/matchmaker.Matchmaker/JoinPlayer',
  grpc.web.MethodType.UNARY,
  proto.matchmaker.JoinRequest,
  proto.matchmaker.Status,
  /**
   * @param {!proto.matchmaker.JoinRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.matchmaker.Status.deserializeBinary
);


/**
 * @param {!proto.matchmaker.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.matchmaker.Status)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.matchmaker.Status>|undefined}
 *     The XHR Node Readable Stream
 */
proto.matchmaker.MatchmakerClient.prototype.joinPlayer =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/matchmaker.Matchmaker/JoinPlayer',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_JoinPlayer,
      callback);
};


/**
 * @param {!proto.matchmaker.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.matchmaker.Status>}
 *     Promise that resolves to the response
 */
proto.matchmaker.MatchmakerPromiseClient.prototype.joinPlayer =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/matchmaker.Matchmaker/JoinPlayer',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_JoinPlayer);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.matchmaker.JoinRequest,
 *   !proto.matchmaker.Status>}
 */
const methodDescriptor_Matchmaker_JoinVisitor = new grpc.web.MethodDescriptor(
  '/matchmaker.Matchmaker/JoinVisitor',
  grpc.web.MethodType.UNARY,
  proto.matchmaker.JoinRequest,
  proto.matchmaker.Status,
  /**
   * @param {!proto.matchmaker.JoinRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.matchmaker.Status.deserializeBinary
);


/**
 * @param {!proto.matchmaker.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.matchmaker.Status)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.matchmaker.Status>|undefined}
 *     The XHR Node Readable Stream
 */
proto.matchmaker.MatchmakerClient.prototype.joinVisitor =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/matchmaker.Matchmaker/JoinVisitor',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_JoinVisitor,
      callback);
};


/**
 * @param {!proto.matchmaker.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.matchmaker.Status>}
 *     Promise that resolves to the response
 */
proto.matchmaker.MatchmakerPromiseClient.prototype.joinVisitor =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/matchmaker.Matchmaker/JoinVisitor',
      request,
      metadata || {},
      methodDescriptor_Matchmaker_JoinVisitor);
};


module.exports = proto.matchmaker;

