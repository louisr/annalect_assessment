import asyncio

from app.database.database import async_engine
from app.models.imports import Base


async def main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("created database")


if __name__ == "__main__":
    asyncio.run(main())
