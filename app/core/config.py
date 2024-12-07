from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # COMMON
    VERSION: str = "v0.0.1"
    ROOT_PATH: str = "/api/v1/fastapi-demo"
    SERVICE_NAME: str = "fastapi-demo"
    PROJECT_NAME: str = "FastAPI Demo"

    # OTEL
    # # TRACER
    TRACER_USING: bool = True
    TRACER_GOOGLE: bool = True
    TRACER_CONSOLE: bool = False
    OTEL_EXPORTER_GCP_TRACE_PROJECT_ID: str = ""

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()