
from pathlib import Path
from django.urls import path 
import os

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SECRET_KEY = 'django-insecure-d@_pt=wu(&eloe91li%andl!c**e*5v^!o@ai@&$kr*j1#-=7-'

DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'MMoRPGapp',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_apscheduler',
    'ckeditor',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_EMAIL = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_VERIFICATION = 'mandatory'

LOGIN_REDIRECT_URL = '../../mmorpg/posts'

ROOT_URLCONF = 'Bulletin_board.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
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

WSGI_APPLICATION = 'Bulletin_board.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFIELDS_DIRS = [
    BASE_DIR / 'static'
]


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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_IMAGE_BACKEND = 'ckeditor_uploader.backend.PillowBackend'

STATIC_URL = '/static/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yangex.ru'
EMAIL_PORT = 465
EMAIL_USE_TSL = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'xenor.lager@gmail.com'
EMAIL_HOST_PASSWORD = 'Fantomas435'
DEFAULT_FROM_EMAIL = 'xenor.lager@gmail.com' 
SERVER_EMAIL = 'xenor.lager@gmail.com'  


EMAIL_SUBJECT_PREFIX = ' '
# ADMINS = [(
#     'Ars', 'stalker.lager@gmail.com'
# )]


CACHES = {
    'default' : {
        'BACKEND' : 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION' : os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT' : 0,
            
    }
} 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
