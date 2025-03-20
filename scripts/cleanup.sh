#!/bin/bash
# cleanup.sh

echo "> 기존 Git 관련 파일 삭제 중..." >> /home/ec2-user/deploy.log

# .git 디렉토리 내 COMMIT_EDITMSG 파일 삭제
rm -f /home/ec2-user/aws-study/.git/COMMIT_EDITMSG || { echo "Git 파일 삭제 실패!"; exit 1; }

# 다른 Git 관련 파일도 삭제가 필요하면 추가 가능
# rm -rf /home/ec2-user/aws-study/.git/*
