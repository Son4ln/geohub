"""Model for order service"""
from datetime import datetime
from typing import List, Literal

from pydantic import BaseModel, Field

# pylint: disable=too-few-public-methods

ORDER_STATUS = Literal["PENDING", "IN-PROGRESs", "COMPLETED"]


class OrderedServiceInput(BaseModel):
    """Ordered service model"""

    service_id: int = Field(..., title="Service ID", example=1)


class OrderedServiceOuput(OrderedServiceInput):
    """Ordered service output model"""

    id: int = Field(..., title="ID", example=1)
    order_id: int = Field(..., title="Order ID", example=1)


class OrderInput(BaseModel):
    """Order input request class"""

    customer_id: int = Field(
        ...,
        title="Id of the customer who ordered",
        example=1,
    )
    employee_id: int = Field(
        ...,
        title="ID of the person handling the order",
        example=1,
    )
    status: ORDER_STATUS = Field(
        ...,
        title="Status of the order",
        example="PENDING",
    )
    note: str = Field(
        ...,
        title="Customer's note",
        example="Call me after done",
    )

    ordered_services: List[OrderedServiceInput] = Field(
        ...,
        title="Ordered Services",
    )


class OrderOutput(OrderInput):
    """Order output request class"""

    id: int = Field(
        ...,
        title="Order's id",
        example=1,
    )

    created_date: datetime = Field(
        ..., title="Date of creation", example=datetime.now()
    )

    ordered_services: List[OrderedServiceOuput] = Field(
        ...,
        title="Ordered Services",
    )
