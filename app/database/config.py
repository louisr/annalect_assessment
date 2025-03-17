import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@db:5432/imports_db"
)

# SQLAlchemy configuration
ASYNC_ENGINE_ARGS = {
    "echo": bool(os.getenv("SQL_ECHO", "False").lower() == "true"),
    "pool_pre_ping": True,
    "pool_size": int(os.getenv("SQL_POOL_SIZE", "5")),
    "max_overflow": int(os.getenv("SQL_MAX_OVERFLOW", "10")),
}
