from db.database import Base, async_engine, async_session_maker
from .models import Category

class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    # @staticmethod
    # async def insert_category():
    #     async with (async_session_maker() as session):
    #         catygoty_one = Category(
    #             name="Умар",
    #             slug = "rttex",
    #             is_active=True,
    #             parent_id=1
    #             )

    #         session.add(catygoty_one)
    #         # flush взаимодействует с БД, поэтому пишем await
    #         await session.flush()
    #         await session.commit()