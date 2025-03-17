from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete

from app.schemas.imports import ImportCreatePayload, ImportUpdatePayload
from app.models.imports import Import


async def create_import(payload: ImportCreatePayload, db: AsyncSession) -> int:
    """
    Create a import record
    """
    data = payload.model_dump(by_alias=False)
    db_import = Import(**data)
    db.add(db_import)
    await db.commit()
    await db.refresh(db_import)
    return db_import.id


async def get_imports(
    skip: int, limit: int, countryName: str, db: AsyncSession
) -> List[Import]:
    """
    Get a list of import record from database
    """
    stmt = select(Import)
    if countryName:
        stmt = stmt.where(
            Import.origin_type_name == "Country",
            Import.origin_name == countryName,
        )
    stmt = stmt.offset(skip).limit(limit)
    query = await db.execute(stmt)
    return query.scalars().all()


async def get_import(import_id: int, db: AsyncSession) -> Import:
    """
    Get a single import record from database
    """
    result = await db.execute(select(Import).where(Import.id == import_id))
    return result.scalars().one()


async def update_import(
    import_id: int, payload: ImportUpdatePayload, db: AsyncSession
) -> dict:
    """
    Update a single import record
    """
    d = payload.model_dump(exclude_unset=True)
    print(d)
    stmt = update(Import).where(Import.id == import_id)
    stmt = stmt.values(**payload.model_dump(exclude_unset=True))
    print(stmt)
    result = await db.execute(stmt)
    await db.commit()
    return result


async def delete_import(import_id: int, db: AsyncSession):
    """
    Delete a single import record
    """
    stmt = delete(Import).where(Import.id == import_id)
    await db.execute(stmt)
    await db.commit()
    return None
