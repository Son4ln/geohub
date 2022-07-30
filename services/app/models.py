"""Model for services(products) service"""
from pydantic import BaseModel, Field

# pylint: disable=too-few-public-methods


class ServiceInput(BaseModel):
    """Service input request class"""

    code: str = Field(
        ...,
        title="Service's code",
        example="GBP",
    )
    name: str = Field(
        ...,
        title="Service's name",
        example="Gold package",
    )
    summary: str = Field(
        ...,
        title="Service summary",
        example="Premium service package",
    )
    description: str = Field(
        ...,
        title="Detailed description of the service",
        example="Detailed description of the service",
    )
    price: int = Field(
        ...,
        title="Price of the service",
        example=100,
    )
    os_platform: str = Field(
        ...,
        title="Platform the service supports",
        example="Windows",
    )


class ServiceOutput(ServiceInput):
    """Service output request class"""

    id: int = Field(
        ...,
        title="Service's id",
        example=1,
    )
