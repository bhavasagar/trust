from .base import *
import os

DEBUG = False

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