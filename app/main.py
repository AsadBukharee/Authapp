from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.logging_config import setup_logging
from app.db.database import engine, Base, init_db
from app.routers import auth, user


# Set up logging
setup_logging()

# Initialize the app
app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Include your routers
app.include_router(auth.auth_router)
app.include_router(user.users_router)


@app.on_event("startup")
async def startup():
    await init_db()


# Event handlers for startup and shutdown
@app.on_event("startup")
async def on_startup():
    # Perform startup actions like creating database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def on_shutdown():
    # Perform shutdown actions
    pass
