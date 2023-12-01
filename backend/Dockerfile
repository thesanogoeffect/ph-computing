FROM python:3.11-slim-bookworm

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive

# Install necessary utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        unzip \
        xvfb \
        openssl \
        curl \
        jq \
        gnupg \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# copy the app
COPY . .

# set environment variables and expose port
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

EXPOSE 8080

CMD exec uvicorn main:app --host 0.0.0.0 --port $PORT 
