"""Customer database."""

import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from app.database import Base

# pylint: disable=too-few-public-methods


class Customer(Base):
    """Customer table."""

    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(15), unique=True)
    email = Column(String(100))
    address = Column(String(255))

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CustomerActivity(Base):
    """Customer activity table."""

    __tablename__ = "customer_activities"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    activity = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self) -> str:
        return f"{self.id} {self.customer_id} {self.activity}"
