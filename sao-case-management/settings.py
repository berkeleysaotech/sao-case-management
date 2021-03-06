import os
import django_heroku
import dj_database_url
import sys

MASTER_BASE_DIR = os.path.dirname(__file__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY')

LOCAL = (sys.argv[1] == 'runserver')

DEBUG = LOCAL

ALLOWED_HOSTS = ['.herokuapp.com']


# Security settings

SECURE_SSL_REDIRECT = not LOCAL

SESSION_COOKIE_SECURE = not LOCAL

CSRF_COOKIE_SECURE = not LOCAL

SECURE_HSTS_SECONDS = 31536000  # one year

SECURE_HSTS_INCLUDE_SUBDOMAINS = not LOCAL

SECURE_CONTENT_TYPE_NOSNIFF = not LOCAL

SECURE_BROWSER_XSS_FILTER = not LOCAL

X_FRAME_OPTIONS = 'DENY'

SECURE_HSTS_PRELOAD = not LOCAL

SESSION_EXPIRE_AT_BROWSER_CLOSE = not LOCAL


# Mail settings

EMAIL_HOST = 'smtp.sendgrid.net'

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']

EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

EMAIL_PORT = 587

EMAIL_USE_TLS = True


# Application definition

INSTALLED_APPS = [
    'cases.apps.CasesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'phonenumber_field',
    'raven.contrib.django.raven_compat',
    'tinymce',
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

ROOT_URLCONF = 'sao-case-management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(MASTER_BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'sao-case-management.wsgi.application'


# Database

if LOCAL:  # Running locally
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'maxlord',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:  # In production
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}


# Password validation

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


# Login urls

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = '/'  # Home page

LOGOUT_REDIRECT_URL = 'login'


# Localization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = False

USE_L10N = True

USE_TZ = True

PHONENUMBER_DB_FORMAT = 'NATIONAL'

PHONENUMBER_DEFAULT_REGION = 'US'


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Heroku configuration

django_heroku.settings(locals())
