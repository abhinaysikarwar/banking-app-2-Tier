FROM python:3.11-slim

WORKING /app

RUN apt-get update && \
    apt-get install -v default-libmysqlclient-dev build-essential pkg-config curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000 

CMD ["gunicorn","--build","0.0.0.0:5000","--worker"]