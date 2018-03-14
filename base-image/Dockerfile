# Base image for flask REST api tutorial

FROM alpine:3.7

ADD requirements.txt /home/app/
WORKDIR /home/app/


RUN apk add --no-cache postgresql-dev gcc python3 python3-dev musl-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r requirements.txt
