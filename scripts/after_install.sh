#!/bin/bash

IMAGE_NAME=my-django-app
CONTAINER_NAME=my-django-app
DOCKERFILE_NAME=DockerfileProd
BUILD_DIR="/home/ec2-user/aws-study/"

cd $BUILD_DIR || exit 1

docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

docker build -t $IMAGE_NAME -f $DOCKERFILE_NAME .
docker run -d --name $CONTAINER_NAME -p 8080:8080 $IMAGE_NAME
