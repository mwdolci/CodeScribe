from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.core.config import settings
from app.routers import code, health
from starlette.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


def create_app() -> FastAPI:
    tags_metadata = [
        {"name": "code", "description": "Opérations liées au code."},
        {"name": "health", "description": "Endpoints de surveillance et statut."},
    ]

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="1.0.0",
        description="API FastAPI + Ollama pour le workshop FAQ locale",
        openapi_tags=tags_metadata,
        swagger_ui_parameters={"displayRequestDuration": True, "defaultModelsExpandDepth": -1},
    )

    # CORS - autoriser les origines de développement courantes (adapter en prod)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "http://localhost:3000", "http://127.0.0.1:3000", "http://127.0.0.1:8000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # personnalisation simple du schéma OpenAPI (logo + servers)
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
        )
        schema.setdefault("info", {})
        schema["info"]["x-logo"] = {"url": "https://avatars.githubusercontent.com/u/1309177?s=200&v=4"}
        schema["servers"] = [{"url": "http://localhost:8000", "description": "Local"}]
        app.openapi_schema = schema
        return app.openapi_schema

    app.openapi = custom_openapi  # type: ignore[assignment]

    app.include_router(health.router)
    app.include_router(code.router)

    app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

    return app
