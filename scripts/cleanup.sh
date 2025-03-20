#!/bin/bash
# cleanup.sh

echo "> 기존 Git 관련 파일 삭제 중..." >> /home/ec2-user/deploy.log

# Git 관련 파일 모두 삭제 (여기서 필요한 부분만 삭제할 수도 있음)
rm -rf /home/ec2-user/aws-study/.git/COMMIT_EDITMSG || { echo "COMMIT_EDITMSG 삭제 실패!"; exit 1; }
rm -rf /home/ec2-user/aws-study/.git/* || { echo "기타 Git 파일 삭제 실패!"; exit 1; }

# 필요 시 추가적인 클린업 작업 수행
# rm -rf /home/ec2-user/aws-study/.git/...