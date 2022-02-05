#!/bin/bash
FROM python:3.10-alpine

WORKDIR /root/data/
COPY ./requirements.txt /root/data/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /root/data/

EXPOSE 8000
CMD ["python3", "./main.py"]
