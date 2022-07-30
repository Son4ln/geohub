"""GRPC SFS Service."""

# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
import grpc

import app.grpc_gen.services_pb2 as pb2
import app.grpc_gen.services_pb2_grpc as pb2_grpc
from app.database import manager as db_manager


class ServiceForSaleServicer(pb2_grpc.SFSService):
    """SFS service."""

    async def GetServiceById(
        self,
        request: pb2.ServiceId,
        context: grpc.aio.ServicerContext,  # pylint: disable=unused-argument
    ) -> pb2.Service:
        """Get service by id."""
        service = await db_manager.get_service_by_id(request.id)
        if service is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Service not found")
            return pb2.Service()
        return pb2.Service(**service.dict())
