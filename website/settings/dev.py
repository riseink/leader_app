from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pi3t%b08sz@v0&n&(b+9zh)s6(6$3+ew6rb+1vo4af3v_n9mqx'

# AWS Settings

# Used to set MEDIA_URL and DEFAULT_FILE_STORAGE accordingly
ENABLE_AWS_MEDIA_STORAGE = True
# Used to set STATICFILES_STORAGE accordingly
ENABLE_AWS_STATIC_STORAGE = False

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


EMAIL_BACKEND = 'django_ses.SESBackend'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Local dev database settings
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE','django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME','wagtail'),
        'USER': os.getenv('DB_USER','postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD','password'),
        'HOST': os.getenv('DB_HOST','pgdb'),
        'PORT': os.getenv('DB_PORT','5432'),
    }
}

ALLOWED_HOSTS = ['localhost', 'scc-wagtail-production.sccdigital.net','sccadv.com','www.sccadv.com','schafercondoncarter.com','www.schafercondoncarter.com']


try:
    from .local import *
except ImportError:
    pass
