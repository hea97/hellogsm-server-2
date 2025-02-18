# Python 기반 이미지 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 코드 복사 및 의존성 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 실행 명령어 설정 (gunicorn 사용)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
