"""Database manager for the order service."""

from typing import List, Union

from sqlalchemy.future import select

from app.database import SQLAsyncSession
from app.database.models import Order, OrderedService
from app.models import OrderedServiceOuput, OrderInput, OrderOutput


async def get_all_orders() -> List[OrderOutput]:
    """Get all orders"""
    async with SQLAsyncSession() as session:
        query = select(Order)
        result = await session.execute(query)
        orders = result.scalars().all()

    return [OrderOutput(**order.__dict__) for order in orders]


async def create_order(payload: OrderInput) -> OrderOutput:
    """Add order to database"""
    async with SQLAsyncSession() as session, session.begin():
        order = Order(
            customer_id=payload.customer_id,
            employee_id=payload.employee_id,
            status=payload.status,
            note=payload.note,
        )
        session.add(order)
        await session.flush()

        service_list = []
        for service in payload.ordered_services:
            ordered_service = OrderedService(
                order_id=order.id, service_id=service.service_id
            )
            service_list.append(ordered_service)

        session.add_all(service_list)
        await session.flush()

        ordered_list = []
        for service in service_list:
            ordered_list.append(OrderedServiceOuput(**service.__dict__))

    return OrderOutput(**order.__dict__, ordered_services=ordered_list)


# async def get_customer_by_phone(phone: str) -> Union[CustomerOutput, None]:
#     """Get customer by phone number"""
#     async with SQLAsyncSession() as session:
#         query = select(Customer).filter(Customer.phone == phone)
#         result = await session.execute(query)
#         customer = result.scalars().first()

#     return CustomerOutput(**customer.__dict__) if customer else None


# async def add_customer_activity(activity: ActivityInput) -> ActivityOutput:
#     """Add customer activity"""
#     async with SQLAsyncSession() as session, session.begin():
#         activity = CustomerActivity(**activity.dict())
#         session.add(activity)
#         await session.flush()

#     return ActivityOutput(**activity.__dict__)


# async def get_customer_activities() -> List[ActivityOutput]:
#     """Get all customer activities"""
#     async with SQLAsyncSession() as session:
#         query = select(CustomerActivity)
#         result = await session.execute(query)
#         activities = result.scalars().all()
#     return [ActivityOutput(**activity.__dict__) for activity in activities]
