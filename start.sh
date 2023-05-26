#!/bin/bash

export OTEL_SERVICE_NAME="creditprocessorservice"
export OTEL_PROPAGATORS="tracecontext,baggage,b3multi"

splunk-py-trace python3 main.py
