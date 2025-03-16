import os
from django.core.exceptions import ImproperlyConfigured

# 환경 변수에서 AWS 키 가져오기
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')  # AWS 접근 키
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')  # AWS 비밀 키

# AWS 키가 환경 변수에 설정되지 않으면 예외 발생
if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise ImproperlyConfigured("AWS_ACCESS_KEY_ID 또는 AWS_SECRET_ACCESS_KEY가 설정되지 않았습니다.")

# AWS S3 설정
AWS_STORAGE_BUCKET_NAME = 'aws-studys'  # 사용할 S3 버킷 이름
AWS_S3_REGION_NAME = 'ap-northeast-2'   # S3 버킷 리전 (서울 리전)
AWS_S3_SIGNATURE_VERSION = 's3v4'  # 서명 버전 설정
AWS_DEFAULT_ACL = None  # 기본 ACL 설정

# S3 객체에 대한 추가 설정
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # 파일 캐시 시간 설정
}

AWS_S3_FILE_OVERWRITE = False  # 기존 파일 덮어쓰기 방지

# Static 파일 설정 (CSS, JS 등)
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # S3 저장소 백엔드

# Media 파일 설정 (업로드된 파일)
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # 기본 파일 저장소 백엔드

# INSTALLED_APPS에 필요한 앱 추가
INSTALLED_APPS = [
    # 기존 앱들
    'django.contrib.staticfiles',  # Static 파일 관련 앱
    'storages',  # S3 사용을 위한 django-storages 추가
]

# Static 파일을 S3에 업로드할 때 사용하는 백엔드 설정
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media 파일을 S3에 업로드할 때 사용하는 백엔드 설정
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
