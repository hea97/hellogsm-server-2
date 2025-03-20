#!/bin/bash
# cleanup.sh

echo "> 기존 Git 파일 삭제 중..." >> /home/ec2-user/deploy.log

# .git 디렉토리의 특정 파일 삭제
rm -rf /home/ec2-user/aws-study/.git/COMMIT_EDITMSG

# 다른 임시 파일도 삭제 필요 시 추가 가능
# rm -rf /home/ec2-user/aws-study/.git/*
