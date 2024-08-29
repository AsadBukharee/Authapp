from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import settings

# Load the database URL from settings
DATABASE_URL = settings.get_database_url()

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create the async session maker
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Declare the base for ORM models
Base = declarative_base()

# Initialize the database, create tables
async def init_db():
    async with engine.begin() as conn:
        # Create all tables defined with Base
        await conn.run_sync(Base.metadata.create_all)

# Dependency for database session
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
