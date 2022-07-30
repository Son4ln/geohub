"""Defind the customers API."""

from typing import List

from fastapi import APIRouter, HTTPException, status

from app.database import manager as db_manager
from app.models import ActivityOutput, CustomerInput, CustomerOutput

customer_router = APIRouter()


@customer_router.post(
    "",
    summary="Create new customer",
    response_model=CustomerOutput,
    status_code=status.HTTP_201_CREATED,
)
async def create_customer(payload: CustomerInput) -> CustomerOutput:
    """Create new customer"""
    if await db_manager.get_customer_by_phone(payload.phone):
        raise HTTPException(
            detail="Customer with this phone number already exists",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    response = await db_manager.create_customer(payload)
    return response


@customer_router.get(
    "/activity",
    summary="Get all customer activities",
    response_model=List[ActivityOutput],
    status_code=status.HTTP_200_OK,
)
async def get_customer_activity() -> List[ActivityOutput]:
    """Get all customer activities"""
    activity = await db_manager.get_customer_activities()
    return activity


@customer_router.get(
    "/{phone}",
    summary="Get customer by phone",
    response_model=CustomerOutput,
    status_code=status.HTTP_200_OK,
)
async def get_customer_by_phone(phone: str) -> CustomerOutput:
    """Get customer by phone."""
    customer = await db_manager.get_customer_by_phone(phone)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    return customer
