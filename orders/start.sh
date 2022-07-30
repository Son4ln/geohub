#!/bin/sh

# grpc generate code
python -m grpc_tools.protoc -I./protos --grpc_python_out=. --python_out=. ./protos/app/grpc_gen/*.proto
# run supervisor with config file
supervisord -c /etc/supervisor/conf.d/supervisord.conf
