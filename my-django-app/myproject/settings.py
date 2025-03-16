# settings.py

# S3 설정을 위한 django-storages 설정 추가
INSTALLED_APPS = [
    # 기존 앱들
    'storages',
]

# AWS S3 설정
AWS_ACCESS_KEY_ID = 'your-access-key-id'  # 실제 AWS 접근 키
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'  # 실제 AWS 비밀 키
AWS_STORAGE_BUCKET_NAME = 'aws-studys'  # 사용할 S3 버킷 이름
AWS_S3_REGION_NAME = 'ap-northeast-2'   # S3 버킷 리전
AWS_S3_SIGNATURE_VERSION = 's3v4'  # 서명 버전 설정
AWS_DEFAULT_ACL = None  # 기본 ACL 설정

# Static 파일 설정
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media 파일 설정
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# S3에 대한 추가 설정 (필요시)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

