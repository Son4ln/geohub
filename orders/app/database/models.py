"""Order database."""

import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Order(Base):
    """Order table."""

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    employee_id = Column(Integer)
    status = Column(String(50))
    note = Column(Text)
    created_date = Column(DateTime, default=datetime.datetime.now)
    ordered_services = relationship("OrderedService", back_populates="orders")

    def __repr__(self) -> str:
        return f"Customer ID: {self.id} - Employee ID: {self.employee_id}"


class OrderedService(Base):
    """Customer activity table."""

    __tablename__ = "ordered_services"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    service_id = Column(Integer)
    order = relationship("Order", back_populates="ordered_services")

    def __repr__(self) -> str:
        return f"Order ID: {self.order_id} - Service ID: {self.service_id}"
