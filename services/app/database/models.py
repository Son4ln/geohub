"""Service database."""

from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Service(Base):
    """Service table."""

    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    code = Column(String(100), unique=True)
    name = Column(String(100))
    summary = Column(String(250))
    description = Column(Text)
    price = Column(Integer)
    os_platform = Column(String(30))

    def __repr__(self) -> str:
        return f"{self.name} - {self.os_platform}"
