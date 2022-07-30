"""Database module."""
import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URI = os.getenv("DATABASE_URI")
# an Engine, which the Session will use for connection
# resources
Engine = create_async_engine(DATABASE_URI)
Base = declarative_base()
# expire_on_commit=False will prevent attributes from being expired
# after commit.
SQLAsyncSession = sessionmaker(Engine, expire_on_commit=False, class_=AsyncSession)
