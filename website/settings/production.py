from .base import *
import dj_database_url

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

EMAIL_BACKEND = 'django_ses.SESBackend'

# AWS Settings

# Used to set MEDIA_URL and DEFAULT_FILE_STORAGE accordingly
ENABLE_AWS_MEDIA_STORAGE = True
# Used to set STATIC_FILE_STORAGE accordingly
ENABLE_AWS_STATIC_STORAGE = True

# AWS Credentials (leave as is)
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '') # Name of the media storage S3 bucket
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')             # User's access key ID (found in credentials.csv)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')     # User's secret access key (found in credentials.csv)

# Domain is determined based on AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/{bucket_name}'.format(bucket_name=AWS_STORAGE_BUCKET_NAME)
# Set to True if s3 bucket URL should use https:// instead of http://
AWS_S3_HTTPS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_LOCATION = 'static'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, STATICFILES_LOCATION),
]

STATIC_ROOT = os.path.join(BASE_DIR, STATICFILES_LOCATION)
STATIC_URL = '/{}/'.format(STATICFILES_LOCATION)

# Use custom storage backend for AWS
if ENABLE_AWS_STATIC_STORAGE:
    STATICFILES_STORAGE = 'storage_backends.StaticS3Storage'


# Media files

MEDIAFILES_LOCATION = 'media'

MEDIA_ROOT = os.path.join(BASE_DIR, MEDIAFILES_LOCATION)
MEDIA_URL = '/{}/'.format(MEDIAFILES_LOCATION)

# Use custom storage backend for AWS
if ENABLE_AWS_MEDIA_STORAGE:
    MEDIA_URL = ('https://' if AWS_S3_HTTPS else 'http://') + AWS_S3_CUSTOM_DOMAIN + MEDIA_URL
    DEFAULT_FILE_STORAGE = 'storage_backends.MediaS3Storage'

if ENABLE_AWS_STATIC_STORAGE:
    STATIC_URL = ('https://' if AWS_S3_HTTPS else 'http://') + AWS_S3_CUSTOM_DOMAIN + STATIC_URL
    STATIC_FILE_STORAGE = 'storage_backends.StaticS3Storage'

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE','django.db.backends.postgresql'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }
DATABASES = {'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))}

ALLOWED_HOSTS = ['*']

# Redirect to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

try:
    from .local import *
except ImportError:
    pass