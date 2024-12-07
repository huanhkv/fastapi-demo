from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logging import Logger
from app.core.config import settings
from app.core.otel import setup_opentelemetry

logger = Logger().get_logger()
logger.info(f"Configurations: {settings}")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    root_path=settings.ROOT_PATH
)

# Middleware
# # CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# OpenTelemetry Setting
setup_opentelemetry(settings)
FastAPIInstrumentor.instrument_app(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)