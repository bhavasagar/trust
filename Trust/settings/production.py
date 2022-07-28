from .base import *
import os


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

ALLOWED_HOSTS = ['voicetrustorg.in']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trust',
        'USER': 'trustuser',
        'PASSWORD': 'password@trust',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30
