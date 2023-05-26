FROM python:3.9-slim

# Set working directory
WORKDIR /app


COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy main app
COPY start.sh .
COPY main.py .

# Bootstrap OTel
#RUN splunk-py-trace-bootstrap

# Set the entrypoint command to run the application
#CMD ["splunk-py-trace", "python3", "main.py"]
#CMD ["python3", "main.py"]
CMD ["./start.sh"]
