from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import (
    Resource, SERVICE_NAME, SERVICE_INSTANCE_ID
)
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from app.core.logging import Logger


def setup_opentelemetry(settings):

    logger = Logger().get_logger()

    resource = Resource.create(attributes={
        SERVICE_NAME: settings.SERVICE_NAME,
        # SERVICE_INSTANCE_ID: ""
    })
    logger.info(f"OTEL Resource: {resource.to_json()}")

    # Tracer
    tracer_provider = TracerProvider(resource=resource)
    logger.info(f"TRACER_USING: {settings.TRACER_USING}")
    if settings.TRACER_USING:
        logger.info(f"\t- TRACER_CONSOLE: {settings.TRACER_CONSOLE}")
        logger.info(f"\t- TRACER_GOOGLE: {settings.TRACER_GOOGLE}")
        # # Console
        if settings.TRACER_CONSOLE:
            from opentelemetry.sdk.trace.export import ConsoleSpanExporter
            processor_console = BatchSpanProcessor(ConsoleSpanExporter())
            tracer_provider.add_span_processor(processor_console)

        # # Google Tracer
        if settings.TRACER_GOOGLE:
            from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
            processor_cloud_trace = BatchSpanProcessor(CloudTraceSpanExporter(
                project_id=settings.OTEL_EXPORTER_GCP_TRACE_PROJECT_ID
            ))
            tracer_provider.add_span_processor(processor_cloud_trace)

    trace.set_tracer_provider(tracer_provider)