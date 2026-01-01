
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

RUN pip install --no-cache-dir \
    fastapi uvicorn[standard] \
    scikit-learn pandas numpy \
    xgboost

COPY . .

EXPOSE 8000

CMD ["uvicorn", "uberAPI:app", "--host", "0.0.0.0", "--port", "8000"]
