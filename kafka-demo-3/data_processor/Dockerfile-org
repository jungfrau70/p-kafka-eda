# syntax=docker/dockerfile:1
FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
COPY config.py .
COPY data_processor.py .

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "data_processor.py", "worker", "-p", "10001"]
