#!/bin/bash

which python
python -m grpc_tools.protoc -I./grpc --python_out=. --grpc_python_out=. ./grpc/dispatcher.proto