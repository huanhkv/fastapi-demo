import time
import logging
from logging.config import dictConfig

from pydantic import BaseModel

from app.core.config import settings


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    tz: str = time.strftime('%z')

    LOGGER_NAME: str = "core"
    LOG_FORMAT: str = (
        f"[%(asctime)s.%(msecs)03d{tz}] [%(levelname)s]"
        f" [%(filename)s:%(funcName)s:%(lineno)d] - %(message)s"
    )
    LOG_LEVEL: str = settings.LOG_LEVEL

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "console": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "console": {
            "formatter": "console",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    }
    loggers: dict = {
        "core": {
            "handlers": [
                "console",
            ],
            "level": LOG_LEVEL
        },
    }


dictConfig(LogConfig().dict())


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = (
                super(Singleton, cls).__call__(*args, **kwargs)
            )
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, logger_name='core'):
        self._logger = logging.getLogger(logger_name)

    def get_logger(self):
        return self._logger