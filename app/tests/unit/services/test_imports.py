import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.imports import (
    create_import,
    get_imports,
    get_import,
    update_import,
    delete_import,
)
from app.schemas.imports import ImportCreatePayload, ImportUpdatePayload


@pytest.mark.asyncio
async def test_create_import(async_session: AsyncSession):
    payload = ImportCreatePayload(
        **{
            "year": 2009,
            "month": 1,
            "originName": "Belize",
            "originTypeName": "Country",
            "destinationName": "EXXONMOBIL REFINING & SPLY CO / BEAUMONT / TX",
            "destinationTypeName": "Refinery",
            "gradeName": "Light Sour",
            "quantity": 61,
        }
    )
    import_id = await create_import(payload, async_session)
    assert import_id is not None


@pytest.mark.asyncio
async def test_get_imports(async_session: AsyncSession):
    db = async_session()
    skip = 0
    limit = 10
    countryName = "CountryName"
    imports = await get_imports(skip, limit, countryName, db)
    assert isinstance(imports, list)


@pytest.mark.asyncio
async def test_get_import(async_session: AsyncSession):
    import_id = 1
    import_record = await get_import(import_id, async_session)
    assert import_record is not None


@pytest.mark.asyncio
async def test_update_import(async_session: AsyncSession):
    import_id = 1
    payload = ImportUpdatePayload(
        **{
            "quantity": 2000,
        }
    )
    result = await update_import(import_id, payload, async_session)
    assert result["rowcount"] == 1


@pytest.mark.asyncio
async def test_delete_import(async_session: AsyncSession):
    import_id = 1
    result = await delete_import(import_id, async_session)
    assert result is None
