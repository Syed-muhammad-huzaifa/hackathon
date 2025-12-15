import os
from pathlib import Path

from fastapi import FastAPI
from dotenv import load_dotenv

from backend.app.routers import chat
from backend.app.middleware import add_cors, logging_middleware, rate_limit_middleware

# Explicitly load the .env located in the backend directory so keys are available
ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Floating Docs Chatbot",
        version="0.1.0",
    )
    app.middleware("http")(logging_middleware)
    app.middleware("http")(rate_limit_middleware)
    add_cors(app)

    @app.get("/healthz", tags=["health"])
    def health() -> dict:
        return {"status": "ok"}

    app.include_router(chat.router)
    return app


app = create_app()
