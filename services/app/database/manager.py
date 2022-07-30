"""Database manager for the servives(products) service"""

from typing import List, Union

from sqlalchemy.future import select

from app.database import SQLAsyncSession
from app.database.models import Service
from app.models import ServiceInput, ServiceOutput


async def create_service(payload: ServiceInput) -> ServiceOutput:
    """Add service to database"""
    async with SQLAsyncSession() as session, session.begin():
        service = Service(**payload.dict())
        session.add(service)
        await session.flush()

    return ServiceOutput(**service.__dict__)


async def get_service_by_id(service_id: int) -> Union[ServiceOutput, None]:
    """Get service by id"""
    async with SQLAsyncSession() as session:
        query = select(Service).filter(Service.id == service_id)
        result = await session.execute(query)
        service = result.scalars().first()

    return ServiceOutput(**service.__dict__) if service else None


async def get_service_by_code(service_code: str) -> Union[ServiceOutput, None]:
    """Get service by id"""
    async with SQLAsyncSession() as session:
        query = select(Service).filter(Service.code == service_code)
        result = await session.execute(query)
        service = result.scalars().first()

    return ServiceOutput(**service.__dict__) if service else None


async def get_services(
    order_by: str,
    sort_asc: bool,
    search_code: Union[str, None],
    search_name: Union[str, None],
) -> List[ServiceOutput]:
    """Get all services"""
    async with SQLAsyncSession() as session:
        query = select(Service)
        if search_code:
            query = query.filter(Service.code.contains(search_code))
        if search_name:
            query = query.filter(Service.name.contains(search_name))
        if sort_asc:
            query = query.order_by(getattr(Service, order_by).asc())
        else:
            query = query.order_by(getattr(Service, order_by).desc())

        result = await session.execute(query)
        services = result.scalars().all()
    return [ServiceOutput(**service.__dict__) for service in services]
