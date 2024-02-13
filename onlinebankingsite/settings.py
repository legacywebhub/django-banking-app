"""
Django settings for onlinebankingsite project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
import  dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
#'django-insecure-=vuv*@%!72*eem!1h8vws=f0-(mnnbtv4fbd78in5l5oxc3-r*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'cloudinary_storage',
    'onlinebankingapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlinebankingsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'onlinebankingsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # For Render or production
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Auth model
AUTH_USER_MODEL = "onlinebankingapp.User"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR / 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR / 'staticfiles')

# Media configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')
# Cloudinary media storage
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
#     'API_KEY': config('CLOUDINARY_API_KEY'),
#     'API_SECRET': config('CLOUDINARY_API_SECRET'),
#     'INVALID_VIDEO_ERROR_MESSAGE': 'Please upload a valid video file.',
# }

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login path
LOGIN_URL = 'banking:login'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Jazzmin dashboard settings
JAZZMIN_SETTINGS = {
    "site_title": "Admin",
    "site_header": "ADMIN",

    # Theme settings
    #"theme": "darkly",  #darkly/flatly
    #"dark_mode_theme": "darkly",
    
    # Logo to use for your site, must be present in static files, used for brand on top left
    #"site_logo": "books/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    #"login_logo": None,
}

# SSL Settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True

'''
# Logger
LOGGING = {
    'version':1,
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['server_file'],
            'level': 'DEBUG',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/debug.log',
           'formatter': 'simple'
        },
        'server_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/debug2.log',
           'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        }
    }
}
'''