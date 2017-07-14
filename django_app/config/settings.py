"""
Django settings for instagram project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/


기능들
    회원 관리 모듈 (member/)
        로그인
        회원가입
        팔로우
        친구찾기
        친구추천
        마이페이지
            내가 올린 글
            내 정보 관리

    글 관련 모듈 (post/)
        뉴스피스
        사진업로드
        댓글달기
        좋아요누르기
        태그달기

    알림 관련 모듈 (noti/)
        팔로워의 글 등록 알림
        댓글 알림



"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# django_app/templates
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# django_app/static
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# django_app/media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custom user (default: auth.User)
AUTH_USER_MODEL = 'member.User'
LOGIN_URL = 'member:login'

# Facebook
FACEBOOK_APP_ID = '1601998296497280'
FACEBOOK_SECRET_CODE = 'e7d66517fdd69f442b95340ac6647b46'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',

    'post',
    'member',
    'utils',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom context processors
                'member.context_processors.forms',
                'utils.context_processors.facebook_info'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instagram',
        'USER': 'ysp',
        'PASSWORD': 'dbstlr07',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ke_u%$x!^k+c=00yg-j199@$v$xo^soh3z#(psfq60#kw&048j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# For EMAIL
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# GMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'space214@gmail.com'
EMAIL_HOST_PASSWORD = 'asdfasdfasdf'
EMAIL_PORT = 587

# Celery
CELERY_BROKER_URL = 'redis://localhost:6379/'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/'
