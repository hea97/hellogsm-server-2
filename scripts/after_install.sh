#!/bin/bash

IMAGE_NAME=my-django-app
CONTAINER_NAME=django-prod-server
DOCKERFILE_NAME=Dockerfile
S3_BUCKET_NAME=aws-studys  # S3 버킷 이름
TAR_FILE=my-django-app.tar.gz

# Git 관련 파일 삭제
echo "> Git 관련 파일 삭제 중..." >> /home/ec2-user/deploy.log
rm -f /home/ec2-user/aws-study/.git/COMMIT_EDITMSG || { echo "COMMIT_EDITMSG 삭제 실패!"; exit 1; }
rm -rf /home/ec2-user/aws-study/.git/* || { echo "기타 Git 파일 삭제 실패!"; exit 1; }

echo "> 현재 실행 중인 Docker 컨테이너 ID 확인" >> /home/ec2-user/deploy.log
CURRENT_CONTAINER_ID=$(docker ps -q -f name=$CONTAINER_NAME)

if [ -z "$CURRENT_CONTAINER_ID" ]
then
  echo "> 현재 구동중인 Docker 컨테이너가 없으므로 종료하지 않습니다." >> /home/ec2-user/deploy.log
else
  echo "> 기존 컨테이너 종료 및 삭제" >> /home/ec2-user/deploy.log
  sudo docker stop $CURRENT_CONTAINER_ID
  sudo docker rm $CURRENT_CONTAINER_ID
fi

echo "> S3에서 최신 이미지 다운로드" >> /home/ec2-user/deploy.log
aws s3 cp s3://$S3_BUCKET_NAME/prod/$TAR_FILE . || { echo "S3 다운로드 실패!"; exit 1; }

echo "> Docker 이미지 로드" >> /home/ec2-user/deploy.log
docker load < $TAR_FILE || { echo "Docker 이미지 로드 실패!"; exit 1; }

echo "> 새 컨테이너 실행" >> /home/ec2-user/deploy.log
docker run -d --name $CONTAINER_NAME -p 8000:8000 --restart always $IMAGE_NAME || { echo "컨테이너 실행 실패!"; exit 1; }

echo "> 배포 완료!" >> /home/ec2-user/deploy.log
