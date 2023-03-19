import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.routes import router

settings = Settings()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting FastAPI...")
    yield
    print("closing")

def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""



    app = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)

    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

    app.include_router(router)

    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)