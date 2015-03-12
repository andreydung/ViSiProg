"""
Django settings for visiprog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# BASE_DIR = os.path.dirname( os.getcwd())
print BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!t(i(9f2$1v=g91k@&msoz1m*vl6ck&t=4aop7+xfkta&*&h_k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'interface',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'visiprog.urls'

WSGI_APPLICATION = 'visiprog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

listimage = [f.rstrip() for f in open(os.path.join(BASE_DIR,'interface/static/Google/list.txt'))]
LISTGOOGLE = {}
for i in range(len(listimage)):
    LISTGOOGLE[i] = listimage[i]

listimage = [f.rstrip() for f in open(os.path.join(BASE_DIR,'interface/static/LLNL2/list.txt'))]
LISTLLNL2 = {}
for i in range(len(listimage)):
    LISTLLNL2[i] = listimage[i]

listimage = [f.rstrip() for f in open(os.path.join(BASE_DIR,'interface/static/LLNL3/list.txt'))]
LISTLLNL3 = {}
for i in range(len(listimage)):
    LISTLLNL3[i] = listimage[i]

IMAGEPATH = '/static/Google/'
LLNL2PATH = '/static/LLNL2/'
LLNL3PATH = '/static/LLNL3/'

STATIC_ROOT = '/var/www/static/'
LOGIN_URL = '/visiprog/login/'

FORCE_SCRIPT_NAME = '/visiprog'
# USE_X_FORWARDED_HOST = True
