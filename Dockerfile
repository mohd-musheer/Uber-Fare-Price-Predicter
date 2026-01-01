# 🚀 Base image
FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update system & install build tools for XGBoost
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Install ML dependencies
RUN pip install --no-cache-dir \
    fastapi uvicorn[standard] \
    scikit-learn pandas numpy \
    xgboost

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "uberAPI:app", "--host", "0.0.0.0", "--port", "8000"]
