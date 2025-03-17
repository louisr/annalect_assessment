from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import async_engine
from app.routers.imports import router as imports_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

    # Close database connections
    await async_engine.dispose()


app = FastAPI(
    title="U.S. Crude Oil Imports Service",
    description="List, filter, and manage U.S. Crude Oil Imports records",
    version="1.0.0",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to U.S. Crude Oil Imports service."}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}


app.include_router(imports_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
