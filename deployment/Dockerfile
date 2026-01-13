FROM python:3.12-slim

ENV TZ=Asia/Taipei

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

ENV APP_VERSION=v1

EXPOSE 7641

