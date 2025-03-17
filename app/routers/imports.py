from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db
from app.schemas.imports import (
    ImportCreatePayload,
    ImportCreateResponse,
    ImportListResponse,
    ImportUpdatePayload,
    ImportSchema,
    ImportUpdateResponse,
)
from app.services import imports as imports_services


router = APIRouter(prefix="/imports", tags=["imports"])


@router.post(
    "/", response_model=ImportCreateResponse, status_code=status.HTTP_201_CREATED
)
async def create_import(
    payload: ImportCreatePayload, db: AsyncSession = Depends(get_db)
):
    import_id = await imports_services.create_import(payload, db)
    return ImportCreateResponse(id=import_id)


@router.get("/", response_model=ImportListResponse)
async def get_imports(
    skip: int = 0,
    limit: int = 100,
    countryName: str = "",
    db: AsyncSession = Depends(get_db),
):
    imports = await imports_services.get_imports(skip, limit, countryName, db)
    return ImportListResponse(results=imports)


@router.get("/{import_id}", response_model=ImportSchema)
async def get_import(import_id: int, db: AsyncSession = Depends(get_db)):
    import_obj = await imports_services.get_import(import_id, db)
    if import_obj is None:
        raise HTTPException(status_code=404, detail="Import not found")
    return ImportSchema.model_validate(import_obj)


@router.patch("/{import_id}", response_model=ImportUpdateResponse)
async def update_import(
    import_id: int, payload: ImportUpdatePayload, db: AsyncSession = Depends(get_db)
):
    import_obj = await imports_services.get_import(import_id, db)
    if import_obj is None:
        raise HTTPException(status_code=404, detail="Import not found")
    result = await imports_services.update_import(import_id, payload, db)
    return {"result": result.rowcount}


@router.delete("/{import_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_import(import_id: int, db: AsyncSession = Depends(get_db)):
    import_obj = await imports_services.get_import(import_id, db)
    if import_obj is None:
        raise HTTPException(status_code=404, detail="Import not found")
    await imports_services.delete_import(import_id, db)
