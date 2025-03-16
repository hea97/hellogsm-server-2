# Python 기반 이미지 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# my-django-app 디렉토리에서 requirements.txt 파일 복사
COPY ./my-django-app/requirements.txt .  # 'my-django-app' 디렉토리에서 requirements.txt 복사

# 의존성 설치
RUN pip install -r requirements.txt

# 애플리케이션 코드 복사
COPY . .  # 현재 디렉토리 내의 모든 파일을 Docker 이미지에 복사

# 실행 명령어 설정 (gunicorn 사용)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
