FROM python:3.10-slim

WORKDIR /app

# System dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for layer caching)
COPY requirements.txt .

# 🔥 IMPORTANT: upgrade pip before installing heavy deps
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy app and model
COPY app ./app
COPY models ./models

# Make sure Python sees /app
ENV PYTHONPATH=/app

# Render sets PORT dynamically
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
