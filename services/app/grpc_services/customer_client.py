"""Services GRPC client."""
import os

import grpc

import app.grpc_gen.customers_pb2 as customer_pb2
import app.grpc_gen.customers_pb2_grpc as customer_pb2_grpc
from app.exceptions import CustomerNotFoundException

CUSTOMER_GRPC_HOST = os.getenv("CUSTOMER_GRPC_HOST")


async def set_customer_activity(customer_id, activity):
    """Set customer activity."""
    async with grpc.aio.insecure_channel(CUSTOMER_GRPC_HOST) as channel:
        stub = customer_pb2_grpc.CustomerServiceStub(channel)
        customer_activity = customer_pb2.CustomerActivity(
            customer_id=customer_id, activity=activity
        )
        try:
            await stub.AddCustomerActivity(customer_activity)
        except grpc.aio.AioRpcError as exception:
            if exception.code() == grpc.StatusCode.NOT_FOUND:
                raise CustomerNotFoundException() from exception
