"""
local settings for development, imported by settings.py
"""

import logging
import os
import os.path


LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')

ALLOWED_HOSTS = [
    '*'
]

DIRNAME = os.path.dirname(os.path.abspath(__file__))

SATCHMO_DIRNAME = DIRNAME

def gettext_noop(string):
    """
    :param string: any string
    :return: that same string
    """
    return string

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', gettext_noop('English')),
)

# These are used when loading the test data
# SITE_NAME = "simple"

DATABASES = {
    'default': {
        # The last part of ENGINE is 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'ado_mssql'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DIRNAME, 'simple.db'),
        # Or path to database file if using sqlite3
        # 'USER': '',             # Not used with sqlite3.
        # 'PASSWORD': '',         # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'EXAMPLE SECRET KEY'

##### For Email ########
# If this isn't set in your settings file, you can set these here
# EMAIL_HOST = 'host here'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'your user here'
# EMAIL_HOST_PASSWORD = 'your password'
# EMAIL_USE_TLS = True

# These are used when loading the test data
SITE_DOMAIN = "localhost"
SITE_NAME = "Simple Satchmo"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'satchmo-cache',
        'TIMEOUT': 60
    }
}
ACCOUNT_ACTIVATION_DAYS = 7


# Configure logging
LOGFILE = "satchmo.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(DIRNAME, LOGFILE),
                    filemode='w')
logging.info("Satchmo Started")
