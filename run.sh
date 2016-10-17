#!/bin/bash

docker-compose kill
docker-compose down

docker-compose up

docker ps -a
