"""FastAPI server for the customer service."""
from fastapi import FastAPI

from app.database import Base, Engine
from app.rest_api.services import service_router

api_app = FastAPI(
    openapi_url="/api/services/openapi.json",
    docs_url="/api/services/docs",
)


async def create_tables():
    """Create database tables."""
    async with Engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@api_app.on_event("startup")
async def startup():
    """Start up service event"""
    await create_tables()


api_app.include_router(service_router, prefix="/services", tags=["services"])
