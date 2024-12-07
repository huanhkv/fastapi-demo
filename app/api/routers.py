import re
import time

from opentelemetry import trace

from fastapi import APIRouter

from app.core.logging import Logger
from app.core.config import settings

tracer = trace.get_tracer(__name__)
logger = Logger().get_logger()


router = APIRouter()


@tracer.start_as_current_span("/health")
@router.get("/health")
async def health_check():
    return {"status": "true"}