'''
Main settings for the project.

ATTENTION:

These settings will not change across deploy environments. So, provide
the settings required to run this project on your environment in your
own local settings files, acording to the example included in the code
tree, "settings/env_example.py", and run the management commands using
the --settings option.

The environment-specific settings files will not be tracked by the
repository, according to the rules on .gitignore. The included example
must NOT be changed since it's part of the project. Instead, copy the
file using a name of your choice and tweak it according to your
environment.

Example:
% cp settings/env_example.py settings/my_settings.py
% ./manage.py runserver --settings=my_settings

Note: if you name your settings file "settings/default.py", you won't
need to provide the 'settings' option to management commands, as
'settings.default' is being expected out of the box.
'''

import os

from django.conf.global_settings import (
    TEMPLATE_CONTEXT_PROCESSORS, MIDDLEWARE_CLASSES,)


DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'ENABLED': False
}

# Language
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Path/URL definitions
PROJECT_PATH = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '..'))
PROJECT_ALIAS = os.path.basename(PROJECT_PATH)
ROOT_URLCONF = 'urls'

# User-uploaded files
MEDIA_ROOT = os.path.join(PROJECT_PATH, '_media')
MEDIA_URL = '/media/'

# Static files
STATIC_ROOT = os.path.join(PROJECT_PATH, '_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# Templates
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS += (
    'constance.context_processors.config',
)

# Deploy
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'pagedown',
    'pagedown',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'gunicorn',
    'sorl.thumbnail',
    'constance',
    'constance.backends.database',

    # Local apps
    'hotsite',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Apps specific settings

# django-constance
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    # Site info
    'SITE_NAME': (u'Site Name', 'Site name'),
    'SITE_DOMAIN': ('siteurl.com', 'Site domain'),
    'SITE_DESCRIPTION': (u'', 'A short site description; will appear on indexers.'),
    'SITE_URL': (u'http://siteurl.com', 'Main site address'),
    'COPYRIGHT_NOTICE': ('', 'Copyright notice'),

    # Google Analytics
    'GA_CODE': ('', 'Google Analytics tracking code'),
    'GA_DOMAIN': ('', 'Google Analytics custom site domain'),

    # Email settings
    'EMAIL_HOST': ('smtp.gmail.com', 'SMTP connection host name'),
    'EMAIL_HOST_USER': ('', 'SMTP host user name'),
    'EMAIL_HOST_PASSWORD': ('', 'SMTP host password'),
    'EMAIL_PORT': (587, 'SMTP connection port'),
    'EMAIL_USE_TLS': (True, 'SMTP uses TLS for connection'),

    # 3rd party
    'FACEBOOK_APP_ID': ('', 'Facebook App ID'),
    'FACEBOOK_GROUP_ID': ('', 'Facebook Group ID'),
}
