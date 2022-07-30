"""Defind the service APIs."""

from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from app.database import manager as db_manager
from app.decorators import track_customer_activity
from app.models import ServiceInput, ServiceOutput

service_router = APIRouter()


@service_router.get(
    "",
    summary="Get all services by some filter",
    response_model=List[ServiceOutput],
    status_code=status.HTTP_200_OK,
)
@track_customer_activity
async def get_services(
    order_by: str = Query("name", description="Sort data by field name"),
    sort_asc: bool = Query(True, description="Sort data ascending or descending"),
    search_code: Optional[str] = Query(None, description="Search services by code"),
    search_name: Optional[str] = Query(None, description="Seacrch services by name"),
    customer_id: int = Query(  # pylint: disable=unused-argument
        None, description="'customer_id' for tracking customer activity"
    ),  # This is for tracking customer activity used in track_customer_activity decorator
) -> List[ServiceOutput]:
    """Get all services by some filter"""
    services = await db_manager.get_services(
        order_by, sort_asc, search_code, search_name
    )
    return services


@service_router.post(
    "",
    summary="Create new service",
    response_model=ServiceOutput,
    status_code=status.HTTP_201_CREATED,
)
async def create_customer(payload: ServiceInput) -> ServiceOutput:
    """Create new service"""
    if await db_manager.get_service_by_code(payload.code):
        raise HTTPException(
            detail="Service with this code already exists",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    response = await db_manager.create_service(payload)
    return response


@service_router.get(
    "/{service_code}",
    summary="Get service by code",
    response_model=ServiceOutput,
    status_code=status.HTTP_200_OK,
)
async def get_service_by_code(service_code: str) -> ServiceOutput:
    """Get service by code."""
    service = await db_manager.get_service_by_code(service_code)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Service not found"
        )
    return service
