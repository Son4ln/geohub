"""Validator for the application."""

from fastapi import HTTPException, status

from app.exceptions import CustomerNotFoundException, ServiceNotFoundException
from app.grpc_services.customer_client import get_customer_by_id
from app.grpc_services.service_client import get_service_by_id


async def check_customer_exists(customer_id: int) -> bool:
    """Check if customer exists."""
    try:
        await get_customer_by_id(customer_id)
    except CustomerNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer ID: {customer_id} not found",
        ) from exception


async def check_service_exists(service_id: int) -> bool:
    """Check if service exists."""
    try:
        await get_service_by_id(service_id)
    except ServiceNotFoundException as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service ID: {service_id} not found",
        ) from exception
