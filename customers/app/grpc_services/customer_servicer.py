"""GRPC Customer Service."""

# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
import grpc
from sqlalchemy.exc import IntegrityError

import app.grpc_gen.customers_pb2 as pb2
import app.grpc_gen.customers_pb2_grpc as pb2_grpc
from app.database import manager as db_manager
from app.models import ActivityInput


class CustomerService(pb2_grpc.CustomerServiceServicer):
    """Customer service."""

    async def AddCustomerActivity(
        self,
        request: pb2.CustomerActivity,
        context: grpc.aio.ServicerContext,  # pylint: disable=unused-argument
    ) -> pb2.CustomerActivity:
        """Add customer activity."""
        activity_input = ActivityInput(
            customer_id=request.customer_id, activity=request.activity
        )
        try:
            await db_manager.add_customer_activity(activity_input)
        except IntegrityError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Customer not found")
        return pb2.CustomerEmpty()

    async def GetCustomerByID(
        self,
        request: pb2.CustomerID,
        context: grpc.aio.ServicerContext,  # pylint: disable=unused-argument
    ) -> pb2.Customer:
        """Get customer by ID."""
        customer = await db_manager.get_customer_by_id(request.id)
        if customer is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Customer not found")
            return pb2.Customer()
        return pb2.Customer(**customer.dict())
