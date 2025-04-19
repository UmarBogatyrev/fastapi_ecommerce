import asyncio
import sys

from models.orm import AsyncORM

async def main():
    await AsyncORM.create_tables()
    #await AsyncORM.insert_category()

if __name__ == "__main__":
    asyncio.run(main())