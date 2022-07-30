"""Database manager for the customer service."""

from typing import List, Union

from sqlalchemy.future import select

from app.database import SQLAsyncSession
from app.database.models import Customer, CustomerActivity
from app.models import ActivityInput, ActivityOutput, CustomerInput, CustomerOutput


async def create_customer(payload: CustomerInput) -> CustomerOutput:
    """Add customer to database"""
    async with SQLAsyncSession() as session, session.begin():
        customer = Customer(**payload.dict())
        session.add(customer)
        await session.flush()

    return CustomerOutput(**customer.__dict__)


async def get_customer_by_phone(phone: str) -> Union[CustomerOutput, None]:
    """Get customer by phone number"""
    async with SQLAsyncSession() as session:
        query = select(Customer).filter(Customer.phone == phone)
        result = await session.execute(query)
        customer = result.scalars().first()

    return CustomerOutput(**customer.__dict__) if customer else None


async def get_customer_by_id(customer_id: int) -> Union[CustomerOutput, None]:
    """Get customer by ID"""
    async with SQLAsyncSession() as session:
        query = select(Customer).filter(Customer.id == customer_id)
        result = await session.execute(query)
        customer = result.scalars().first()

    return CustomerOutput(**customer.__dict__) if customer else None


async def add_customer_activity(activity: ActivityInput) -> ActivityOutput:
    """Add customer activity"""
    async with SQLAsyncSession() as session, session.begin():
        activity = CustomerActivity(**activity.dict())
        session.add(activity)
        await session.flush()

    return ActivityOutput(**activity.__dict__)


async def get_customer_activities() -> List[ActivityOutput]:
    """Get all customer activities"""
    async with SQLAsyncSession() as session:
        query = select(CustomerActivity)
        result = await session.execute(query)
        activities = result.scalars().all()
    return [ActivityOutput(**activity.__dict__) for activity in activities]
