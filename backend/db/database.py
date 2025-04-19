from typing import Annotated

from sqlalchemy import String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .config import settings


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True, # отображение в консоль все запросы к базе
    # pool_size=5, # количество потоков для выполнения запросов
    # max_overflow=10, # количество запросов, которые могут быть вызваны дополнительно
)

async_session_maker = async_sessionmaker(bind=async_engine)


str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }