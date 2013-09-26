# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['DJANGO_SECRET']
except:
    SECRET_KEY = 'f@!&-fi*cnctjrgsf**&@ct$fa2ym1&9@8%-8#2-&h2l9270n#'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    DEBUG = bool(int(os.environ['DJANGO_DEBUG']))
except:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['stregsystem.fklub.dk']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stregsystem.urls'

WSGI_APPLICATION = 'stregsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

import dj_database_url
if len(dj_database_url.config()) > 0:
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

_ = lambda s: s

LANGUAGE_CODE = 'da-DK'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
