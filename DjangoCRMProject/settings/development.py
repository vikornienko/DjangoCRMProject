# https://www.digitalocean.com/community/tutorials/how-to-harden-your-production-django-project

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
        'TEST': { # test database settings
            'NAME': os.path.join(BASE_DIR,  'db_test.sqlite3'), # test database name
        },
    }
}