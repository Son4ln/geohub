"""Model for customer service"""
from datetime import datetime

from pydantic import BaseModel, Field

# pylint: disable=too-few-public-methods


class CustomerInput(BaseModel):
    """Customer input request class"""

    first_name: str = Field(
        ...,
        title="Customer's first name",
        example="John",
    )
    last_name: str = Field(
        ...,
        title="Customer's last name",
        example="Doe",
    )
    phone: str = Field(
        ...,
        title="Customer's phone number",
        example="09091234567",
    )
    email: str = Field(
        ...,
        title="Customer's email address",
        example="joind@gmail.com",
    )
    address: str = Field(
        ...,
        title="Customer's address",
        example="123 Main St, New York, NY 10001",
    )


class CustomerOutput(CustomerInput):
    """Customer output request class"""

    id: int = Field(
        ...,
        title="Customer's id",
        example=1,
    )


class ActivityInput(BaseModel):
    """Activity input request class"""

    customer_id: int = Field(
        ...,
        title="Customer's id",
        example=1,
    )

    activity: str = Field(
        ...,
        title="Customer's activity",
        example="Visited",
    )


class ActivityOutput(ActivityInput):
    """Activity output request class"""

    id: int = Field(
        ...,
        title="Activity's id",
        example=1,
    )

    timestamp: datetime = Field(
        ...,
        title="Time that user do action",
        example="2022-01-19 03:14:07",
    )
