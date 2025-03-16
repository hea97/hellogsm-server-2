import os
from django.core.exceptions import ImproperlyConfigured

# 환경 변수에서 AWS 키 가져오기
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise ImproperlyConfigured("AWS_ACCESS_KEY_ID 또는 AWS_SECRET_ACCESS_KEY가 설정되지 않았습니다.")

AWS_STORAGE_BUCKET_NAME = 'aws-studys'  # 사용할 S3 버킷 이름
AWS_S3_REGION_NAME = 'ap-northeast-2'   # S3 버킷 리전
AWS_S3_SIGNATURE_VERSION = 's3v4'  # 서명 버전 설정
AWS_DEFAULT_ACL = None  # 기본 ACL 설정

# S3에 대한 추가 설정 (필요시)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_S3_FILE_OVERWRITE = False  # 기존 파일 덮어쓰기 방지

# Static 파일 설정 (CSS, JS 등)
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media 파일 설정 (업로드된 파일)
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

INSTALLED_APPS = [
    # 기존 앱들
    'django.contrib.staticfiles',  # 이 앱이 있어야 collectstatic 명령어가 작동합니다.
    'storages',  # S3 사용을 위한 django-storages 추가
]
