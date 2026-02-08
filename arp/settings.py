import os
from pathlib import Path
from corsheaders.defaults import default_headers

import configparser
config = configparser.ConfigParser()
config.read("app.properties")


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-u7!c^1%+)lr%m_li4(vops!+u^hqato2zami-7+&^gj28*7)2m'

DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    CORS_ALLOWED_ORIGINS = [ "http://localhost:3000", "http://127.0.0.1:3000" ]
else:
    ALLOWED_HOSTS = ["aravindpillai.com", "be.aravindpillai.com"]
    CORS_ALLOWED_ORIGINS = ["https://aravindpillai.com", "https://www.aravindpillai.com" ]

CORS_ALLOW_HEADERS = list(default_headers) + ['token', 'name']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'qchat',
    'anonymous',
    'textbox'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'arp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'arp.wsgi.application'

    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

POSTGRES = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": config["database"]["dbname"],
    "USER": config["database"]["username"],
    "PASSWORD": config["database"]["password"],
    "HOST": config["database"]["host"],
    "PORT": config["database"]["port"],
    "CONN_MAX_AGE": 60,
    "OPTIONS": {"sslmode": "require"}
}

DATABASES = {
    'default': SQLLITE if DEBUG else POSTGRES  
}


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
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


QCHAT_ADMIN_PW = config["qchat"]["adminpassword"]
QCHAT_PANICPW = config["qchat"]["panicpw"]
QCHAT_ENCRYPTION_IV = config["qchat"]["iv"]
ANONYMOUS_PW = config["anonymous"]["password"]

EMAIL_ACCOUNTS = {
    "default": {
        "HOST": "smtp.gmail.com",
        "PORT": 587,
        "USE_TLS": True,
        "USER": config["email"]["email"],
        "PASSWORD": config["email"]["password"],
    },
    "qchat": {
        "HOST": "smtp.gmail.com",
        "PORT": 587,
        "USE_TLS": True,
        "USER": config["qchat"]["email"],
        "PASSWORD": config["qchat"]["password"],
    }
}