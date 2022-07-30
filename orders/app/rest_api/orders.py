"""Defind the order APIs."""

from typing import List

from fastapi import APIRouter, status

from app.database import manager as db_manager
from app.models import OrderInput, OrderOutput
from app.validators import check_customer_exists, check_service_exists

order_router = APIRouter()


@order_router.post(
    "",
    summary="Create new order",
    response_model=OrderOutput,
    status_code=status.HTTP_201_CREATED,
)
async def create_order(payload: OrderInput) -> OrderOutput:
    """Create new customer"""
    await check_customer_exists(payload.customer_id)
    for service in payload.ordered_services:
        await check_service_exists(service.service_id)
    response = await db_manager.create_order(payload)
    return response
