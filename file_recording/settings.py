# -*- coding: utf-8 -*-
"""
Django settings for file_recording project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import configparser
import os
import socket


config = configparser.ConfigParser(allow_no_value=True)

ROOT = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ======================
# = Environment config =
# ======================

# If the host name starts with 'ip', load configparser from "production.cfg"

if socket.gethostname().startswith('ip'):
    config.read('%s/production.cfg' % BASE_DIR)
    print('production config')
    ENV = 'PROD'
else:
    config.read('%s/development.cfg' % BASE_DIR)
    print('development config')
    ENV = 'DEV'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-(k7w8z88&j(3qyv(99r7997#^)2=5zadrujfm8hxa1mbv5!el'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get('general', 'DEBUG')

ALLOWED_HOSTS = ['13.126.53.179',]
MEDIA_ROOT = BASE_DIR + '/file_recording/document/docs/'
MEDIA_URL = 'documents/docs/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'file_recording.user',
    'rest_framework',
    'file_recording.updates',
    'file_recording.employee',
    'django_cron',
    'file_recording.schemes',
    'file_recording.registration',
    'file_recording.document',
    'file_recording.result',
    'cronjobs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CRON_CLASSES = [
    'file_recording.user.cron.AutoLogout',
    'file_recording.result.cron.ResultDraw'
]

ROOT_URLCONF = 'file_recording.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'file_recording.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DB_NAME = config.get('db', 'NAME')
DB_USER = config.get('db', 'USER')
DB_PASSWORD = config.get('db', 'PASSWORD')
DB_HOST = config.get('db', 'HOST')
DB_PORT = config.get('db', 'PORT')

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 500,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': int(DB_PORT),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR,'static')

# fs = FileSystemStorage(location=MEDIA_ROOT)
