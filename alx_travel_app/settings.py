import os
from pathlib import Path
import environ
import os

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'amqp://localhost')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Read .env file if present

# Base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Secret Key (set it in .env for security)
SECRET_KEY = env('SECRET_KEY')

# Debug mode
DEBUG = env.bool('DEBUG', default=True)

# Allowed Hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # For handling CORS
    'rest_framework',  # For building APIs
    'drf_yasg',  # For API documentation
    'listings',  # Your app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # For handling CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

# Database configuration using MySQL and environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', default='3306'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins, can be restricted later

# Swagger API documentation URL
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'DOC_EXPANSION': 'none',
    'DEFAULT_MODEL_RENDERER': 'rest_framework.renderers.BrowsableAPIRenderer',
}

# Celery settings for asynchronous task queue (for future use)
CELERY_BROKER_URL = 'amqp://localhost'  # RabbitMQ URL
CELERY_RESULT_BACKEND = 'rpc://'  # Using RPC as backend for task results

# Logging configuration (optional, useful for debugging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# The URL for the API docs via Swagger
SWAGGER_URL = '/swagger/'

