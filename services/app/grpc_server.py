"""GRPC server for SFS service."""
import asyncio
import logging

import grpc

import app.grpc_gen.services_pb2_grpc as pb2_grpc
from app.grpc_services.service_servicer import ServiceForSaleServicer


async def serve():
    """Start the server."""
    server = grpc.aio.server()
    pb2_grpc.add_SFSServiceServicer_to_server(ServiceForSaleServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
