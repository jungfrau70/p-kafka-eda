# syntax=docker/dockerfile:1
FROM python:3.6.15-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY data_requester.py .

CMD [ "python3", "data_requester.py", "worker", "-p", "10001"]
