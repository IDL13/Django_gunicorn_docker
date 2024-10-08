from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ["*"]

    # ALLOWED_HOSTS = ["79.174.84.224", "sch-stock.ru"]
else:
    ALLOWED_HOSTS = ["79.174.84.224", "sch-stock.ru"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'school.apps.SchoolConfig',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if DEBUG:
    DATABASES = {

        'default': {
            'ENGINE': os.getenv("TEST_ENGINE"),
            'NAME': os.getenv("TEST_NAME"),
            'USER': os.getenv("TEST_USER"),
            'PASSWORD': os.getenv("TEST_PASSWORD"),
            'HOST': os.getenv("TEST_HOST"),
            'PORT': os.getenv("TEST_PORT"),
        }
    }

    # DATABASES = {

    #     'default': {
    #         'ENGINE': os.getenv("ENGINE"),
    #         'NAME': os.getenv("NAME"),
    #         'USER': os.getenv("USER"),
    #         'PASSWORD': os.getenv("PASSWORD"),
    #         'HOST': os.getenv("HOST"),
    #         'PORT': os.getenv("PORT"),
    #     }
    # }
else:
   DATABASES = {

        'default': {
            'ENGINE': os.getenv("ENGINE"),
            'NAME': os.getenv("NAME"),
            'USER': os.getenv("USER"),
            'PASSWORD': os.getenv("PASSWORD"),
            'HOST': os.getenv("HOST"),
            'PORT': os.getenv("PORT"),
        }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
if DEBUG:
    STATIC_URL = "mysite/school/static/"
    STATIC_ROOT = "/static/"
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    ]

    # STATIC_URL = '/static/'
    # STATIC_ROOT = os.path.join(BASE_DIR, "static")
    # CSRF_TRUSTED_ORIGINS = ["https://sch-stock.ru"]
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    CSRF_TRUSTED_ORIGINS = ["https://sch-stock.ru"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

