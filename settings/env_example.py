'''
ATTENTION:
This is an example for environment-specific settings. Read the note on
settings/__init__.py to learn how to use this file and run the project.
'''

import sys

from settings import *  # Load main settings


MANAGERS = ADMINS = (
    (u'Developer Name', 'developer@email.com'),
)

CONSTANCE_CONFIG = {
    # Site info
    'SITE_NAME': (u'Site Name', 'Site name'),
    'SITE_URL': (u'http://siteurl.com', 'Main site address'),

    # Email settings
    'EMAIL_HOST': ('smtp.gmail.com', 'SMTP connection host name'),
    'EMAIL_HOST_USER': ('', 'SMTP host user name'),
    'EMAIL_HOST_PASSWORD': ('', 'SMTP host password'),
    'EMAIL_PORT': (587, 'SMTP connection port'),
    'EMAIL_USE_TLS': (True, 'SMTP uses TLS for connection'),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + (
            'sqlite3' if 'test' in sys.argv else 'postgresql_psycopg2'),
        'NAME': '',
    },
}

DEBUG = True

SITE_ID = 1

SECRET_KEY = 'PUT A SECRET CODE HERE'

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211']
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLED': True,
}
