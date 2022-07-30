"""Service GRPC client"""
import os

import grpc

import app.grpc_gen.services_pb2 as service_pb2
import app.grpc_gen.services_pb2_grpc as service_pb2_grpc
from app.exceptions import ServiceNotFoundException

SERVICE_GRPC_HOST = os.getenv("SFS_GRPC_HOST")


async def get_service_by_id(service_id: int) -> service_pb2.Service:
    """get service by id."""
    async with grpc.aio.insecure_channel(SERVICE_GRPC_HOST) as channel:
        stub = service_pb2_grpc.SFSServiceStub(channel)
        customer_id = service_pb2.ServiceId(id=service_id)
        try:
            return await stub.GetServiceById(customer_id)
        except grpc.aio.AioRpcError as exception:
            if exception.code() == grpc.StatusCode.NOT_FOUND:
                raise ServiceNotFoundException() from exception
