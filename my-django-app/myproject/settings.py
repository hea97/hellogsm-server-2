from .settings import *

DEBUG = False

# 프로덕션 환경에서 허용할 호스트
ALLOWED_HOSTS = ['yourdomain.com', '3.34.253.238']

# PostgreSQL 데이터베이스 설정 (실제 DB 정보로 수정)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',        # 실제 DB 이름
        'USER': 'your_db_user',        # 실제 DB 사용자명
        'PASSWORD': 'your_db_password',# 실제 DB 비밀번호
        'HOST': 'your_db_host',        # 데이터베이스 호스트 (localhost 또는 DB 서버 주소)
        'PORT': 'your_db_port',        # PostgreSQL의 포트 (기본값: 5432)
    }
}

# 정적 파일과 미디어 파일을 저장할 디렉토리 경로 설정
STATIC_ROOT = '/path/to/your/static'  # 실제 경로로 수정
MEDIA_ROOT = '/path/to/your/media'    # 실제 경로로 수정

# 기타 기본 설정
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# 만약 Gunicorn이나 다른 프로덕션 서버를 사용한다면 WSGI 설정도 고려해야 합니다.
