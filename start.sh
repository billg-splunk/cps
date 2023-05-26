#!/bin/bash

export OTEL_SERVICE_NAME="creditprocessorservice"
export OTEL_PROPAGATORS="tracecontext,baggage,b3multi"
export OTEL_EXPORTER_OTLP_ENDPOINT="http://$(NODE_IP):4317"

splunk-py-trace python3 main.py
