# syntax=docker/dockerfile:1
FROM python:3.8-alpine

WORKDIR /usr/src/api

COPY requirements.txt .
COPY config.py .
COPY main.py .
COPY schema.py .

RUN python3 -m pip install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
