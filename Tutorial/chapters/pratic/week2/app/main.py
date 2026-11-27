from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from .routers.notes import router

WEEK_DIR = Path(__file__).resolve().parents[1]


def create_app(db_path: Path = WEEK_DIR / "data" / "app.db") -> FastAPI:
    app = FastAPI(title="Week 2 Action Item Extractor")
    app.state.db_path = db_path
    app.include_router(router)

    @app.get("/", include_in_schema=False)
    def index():
        return FileResponse(WEEK_DIR / "frontend" / "index.html", media_type="text/html")

    return app


app = create_app()
