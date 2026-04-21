"""
Работа с сессий
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

session_cls = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
