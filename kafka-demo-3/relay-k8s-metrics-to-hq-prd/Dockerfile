# syntax=docker/dockerfile:1
FROM python:3.6.15-slim-buster

WORKDIR /app

COPY requirements-docker.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY relay-k8s-metrics-to-hq-prd.py .

CMD [ "python3", "relay-k8s-metrics-to-hq-prd.py"]