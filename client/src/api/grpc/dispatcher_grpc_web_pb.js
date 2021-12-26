/**
 * @fileoverview gRPC-Web generated client stub for dispatcher
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = {};
proto.dispatcher = require('./dispatcher_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.dispatcher.DispatcherClient =
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
proto.dispatcher.DispatcherPromiseClient =
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
 *   !proto.dispatcher.User,
 *   !proto.dispatcher.Game>}
 */
const methodDescriptor_Dispatcher_GetGameList = new grpc.web.MethodDescriptor(
  '/dispatcher.Dispatcher/GetGameList',
  grpc.web.MethodType.SERVER_STREAMING,
  proto.dispatcher.User,
  proto.dispatcher.Game,
  /**
   * @param {!proto.dispatcher.User} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.dispatcher.Game.deserializeBinary
);


/**
 * @param {!proto.dispatcher.User} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.dispatcher.Game>}
 *     The XHR Node Readable Stream
 */
proto.dispatcher.DispatcherClient.prototype.getGameList =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/dispatcher.Dispatcher/GetGameList',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_GetGameList);
};


/**
 * @param {!proto.dispatcher.User} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.dispatcher.Game>}
 *     The XHR Node Readable Stream
 */
proto.dispatcher.DispatcherPromiseClient.prototype.getGameList =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/dispatcher.Dispatcher/GetGameList',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_GetGameList);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.dispatcher.User,
 *   !proto.dispatcher.Game>}
 */
const methodDescriptor_Dispatcher_CreateGame = new grpc.web.MethodDescriptor(
  '/dispatcher.Dispatcher/CreateGame',
  grpc.web.MethodType.UNARY,
  proto.dispatcher.User,
  proto.dispatcher.Game,
  /**
   * @param {!proto.dispatcher.User} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.dispatcher.Game.deserializeBinary
);


/**
 * @param {!proto.dispatcher.User} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.dispatcher.Game)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.dispatcher.Game>|undefined}
 *     The XHR Node Readable Stream
 */
proto.dispatcher.DispatcherClient.prototype.createGame =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/dispatcher.Dispatcher/CreateGame',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_CreateGame,
      callback);
};


/**
 * @param {!proto.dispatcher.User} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.dispatcher.Game>}
 *     Promise that resolves to the response
 */
proto.dispatcher.DispatcherPromiseClient.prototype.createGame =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/dispatcher.Dispatcher/CreateGame',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_CreateGame);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.dispatcher.Game,
 *   !proto.dispatcher.Status>}
 */
const methodDescriptor_Dispatcher_CloseGame = new grpc.web.MethodDescriptor(
  '/dispatcher.Dispatcher/CloseGame',
  grpc.web.MethodType.UNARY,
  proto.dispatcher.Game,
  proto.dispatcher.Status,
  /**
   * @param {!proto.dispatcher.Game} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.dispatcher.Status.deserializeBinary
);


/**
 * @param {!proto.dispatcher.Game} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.dispatcher.Status)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.dispatcher.Status>|undefined}
 *     The XHR Node Readable Stream
 */
proto.dispatcher.DispatcherClient.prototype.closeGame =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/dispatcher.Dispatcher/CloseGame',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_CloseGame,
      callback);
};


/**
 * @param {!proto.dispatcher.Game} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.dispatcher.Status>}
 *     Promise that resolves to the response
 */
proto.dispatcher.DispatcherPromiseClient.prototype.closeGame =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/dispatcher.Dispatcher/CloseGame',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_CloseGame);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.dispatcher.JoinRequest,
 *   !proto.dispatcher.Status>}
 */
const methodDescriptor_Dispatcher_JoinPlayer = new grpc.web.MethodDescriptor(
  '/dispatcher.Dispatcher/JoinPlayer',
  grpc.web.MethodType.UNARY,
  proto.dispatcher.JoinRequest,
  proto.dispatcher.Status,
  /**
   * @param {!proto.dispatcher.JoinRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.dispatcher.Status.deserializeBinary
);


/**
 * @param {!proto.dispatcher.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.dispatcher.Status)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.dispatcher.Status>|undefined}
 *     The XHR Node Readable Stream
 */
proto.dispatcher.DispatcherClient.prototype.joinPlayer =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/dispatcher.Dispatcher/JoinPlayer',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_JoinPlayer,
      callback);
};


/**
 * @param {!proto.dispatcher.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.dispatcher.Status>}
 *     Promise that resolves to the response
 */
proto.dispatcher.DispatcherPromiseClient.prototype.joinPlayer =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/dispatcher.Dispatcher/JoinPlayer',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_JoinPlayer);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.dispatcher.JoinRequest,
 *   !proto.dispatcher.Status>}
 */
const methodDescriptor_Dispatcher_JoinVisitor = new grpc.web.MethodDescriptor(
  '/dispatcher.Dispatcher/JoinVisitor',
  grpc.web.MethodType.UNARY,
  proto.dispatcher.JoinRequest,
  proto.dispatcher.Status,
  /**
   * @param {!proto.dispatcher.JoinRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.dispatcher.Status.deserializeBinary
);


/**
 * @param {!proto.dispatcher.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.dispatcher.Status)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.dispatcher.Status>|undefined}
 *     The XHR Node Readable Stream
 */
proto.dispatcher.DispatcherClient.prototype.joinVisitor =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/dispatcher.Dispatcher/JoinVisitor',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_JoinVisitor,
      callback);
};


/**
 * @param {!proto.dispatcher.JoinRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.dispatcher.Status>}
 *     Promise that resolves to the response
 */
proto.dispatcher.DispatcherPromiseClient.prototype.joinVisitor =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/dispatcher.Dispatcher/JoinVisitor',
      request,
      metadata || {},
      methodDescriptor_Dispatcher_JoinVisitor);
};


module.exports = proto.dispatcher;

