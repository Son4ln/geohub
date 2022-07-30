"""FastAPI server for the order service."""
from fastapi import FastAPI

from app.database import Base, Engine
from app.rest_api.orders import order_router

api_app = FastAPI(
    openapi_url="/api/orders/openapi.json",
    docs_url="/api/orders/docs",
)


async def create_tables():
    """Create database tables."""
    async with Engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@api_app.on_event("startup")
async def startup():
    """Start up service event"""
    await create_tables()


api_app.include_router(order_router, prefix="/orders", tags=["orders"])
