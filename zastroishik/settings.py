#"host""
#Django settings for zastroishik project.

#Generated by 'django-admin startproject' using Django 2.1.2.

#For more information on this file, see
#https://docs.djangoproject.com/en/2.1/topics/settings/

#For the full list of settings and their values, see
#https://docs.djangoproject.com/en/2.1/ref/settings/
#"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = '/var/www/zastr/' #os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!&+(sq$8%5*tpw#wtvyq%2im*dt6*-zaq*p@&uz*ug32&)a-b6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['77.222.60.205','grand-park-sochi.ru', 'grandparksochi.ru','zhk-grand-park-sochi.ru','zhk-grand-park.ru','zhkgrandpark.ru',
'zhkgrandparksochi.ru','xn-----6kcbmh5aoxphhgq5g.xn--p1ai','xn--80aahfvlslggfn3f.xn--p1ai','xn-------63dbsjfiwjdpbgfds0akdnljvgsm5p.xn--p1ai',
'xn------7cdbpiehulnbgddqyidwjsgp.xn--p1ai','xn--80aahfcfoijbedcnuhcthqfo.xn--p1ai','xn--80aahfcfofdkbeecovickkhsfqj1n.xn--p1ai',
'xn------6cdbpimzmg6askkgt3i.xn--p1ai','xn--80aahfhyevtgf.xn--p1ai','xn--80aahfhqjeyniifp5g.xn--p1ai',
'www.grand-park-sochi.ru', 'www.grandparksochi.ru','www.zhk-grand-park-sochi.ru','www.zhk-grand-park.ru','www.zhkgrandpark.ru',
'www.zhkgrandparksochi.ru','www.xn-----6kcbmh5aoxphhgq5g.xn--p1ai','www.xn--80aahfvlslggfn3f.xn--p1ai','www.xn-------63dbsjfiwjdpbgfds0akdnljvgsm5p.xn--p1ai',
'www.xn------7cdbpiehulnbgddqyidwjsgp.xn--p1ai','www.xn--80aahfcfoijbedcnuhcthqfo.xn--p1ai','www.xn--80aahfcfofdkbeecovickkhsfqj1n.xn--p1ai',
'www.xn------6cdbpimzmg6askkgt3i.xn--p1ai','www.xn--80aahfhyevtgf.xn--p1ai','www.xn--80aahfhqjeyniifp5g.xn--p1ai']


# Application definition

INSTALLED_APPS = [
    #'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flats.apps.FlatsConfig',
    'zayavka.apps.ZayavkaConfig',
    'blog.apps.BlogConfig',
    'phonenumber_field',
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

ROOT_URLCONF = 'zastroishik.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'flats.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'zastroishik.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

PHONENUMBER_DB_FORMAT = 'E164'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'zhem-otchet@mail.ru'
EMAIL_HOST_PASSWORD = 'UoAAb^atr4N3'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
MEDIA_ROOT = '/var/www/zastr/image/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'image')
#STATICFILES_DIRS = (
#   '/var/www/zastr/static/'
#)
MEDIA_URL = '/'

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/zastr/static1/'
#STATIC_ROOT = '/home/hamster197/zhem1/zastr/zastroyshiki/image/'
