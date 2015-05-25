"""
Django settings for ni project.
"""


import os
import sys

DIRNAME = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))
BASENAME = os.path.dirname(DIRNAME)

sys.path.append(os.path.join(BASENAME, 'satchmo'))

DJANGO_PROJECT = 'store'
DJANGO_SETTINGS_MODULE = 'ni.ci_settings'

ADMINS = (
    ('', ''),
    # tuple (name, email) - important for error reports sending, if DEBUG is disabled.
)

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# Image files will be stored off of this path
#
# If you are using Windows, recommend using normalize_path() here
#
# from satchmo_utils.thumbnail import normalize_path
# MEDIA_ROOT = normalize_path(os.path.join(DIRNAME, 'static/'))
MEDIA_ROOT = os.path.join(DIRNAME, '..', 'media/')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = "/media/"

# STATIC_ROOT can be whatever different from other dirs
STATIC_ROOT = os.path.join(DIRNAME, '..', 'static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'static/'),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    'compressor.finders.CompressorFinder'
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'  # remove for Django 1.4 as deprecated

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&jrnmg5)=ja@ioe1vhy51^j0hupv#!6nn4hr_poqs6go_iixkz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'ni.middleware.LoggingMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    # "satchmo_ext.recentlist.middleware.RecentProductMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# this is used to add additional config variables to each request
# NOTE: If you enable the recent_products context_processor, you MUST have the
# 'satchmo_ext.recentlist' app installed.
TEMPLATE_CONTEXT_PROCESSORS = (
    'satchmo_store.shop.context_processors.settings',
    'django.contrib.auth.context_processors.auth',
    # 'satchmo_ext.recentlist.context_processors.recent_products',
    # do not forget following. Maybe not so important currently
    # but will be
    'django.core.context_processors.media',  # MEDIA_URL
    'django.core.context_processors.static',  # STATIC_URL
    'django.contrib.messages.context_processors.messages',

    # Allauth crap
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

ROOT_URLCONF = 'ni.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.sites',
    'satchmo_store.shop',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_comments',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'haystack',

    # Authentication here
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'sorl.thumbnail',
    'keyedcache',
    'l10n',
    'livesettings',
    'satchmo_utils.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    # 'satchmo_store.contact.supplier',
    # 'shipping.modules.tiered',
    # 'satchmo_ext.newsletter',
    # 'satchmo_ext.recentlist',
    'product',
    'product.modules.configurable',
    'product.modules.custom',
    # 'product.modules.downloadable',
    # 'product.modules.subscription',
    # 'satchmo_ext.product_feeds',
    # 'satchmo_ext.brand',
    'payment',
    'payment.modules.dummy',
    # 'payment.modules.purchaseorder',
    # 'payment.modules.giftcertificate',
    # 'satchmo_ext.wishlist',
    # 'satchmo_ext.upsell',
    'satchmo_ext.productratings',
    'satchmo_ext.satchmo_toolbar',
    'satchmo_utils',
    # 'shipping.modules.tieredquantity',
    # 'satchmo_ext.tieredpricing',
    'debug_toolbar',
    'app_plugins',
    'compressor',
    'ni'
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://solr.clowntown.me:8983/solr/ni',
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
    'django.contrib.auth.backends.ModelBackend',
)

# DEBUG_TOOLBAR_CONFIG = {
# 'INTERCEPT_REDIRECTS' : False,
# }

#### Satchmo unique variables ####
# from django.conf.urls import patterns, include
SATCHMO_SETTINGS = {
    'SHOP_BASE': '',
    'MULTISHOP': False,
    'DOCUMENT_CONVERTER': 'shipping.views.HTMLDocument',
    # 'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

SKIP_SOUTH_TESTS = True

LIVESETTINGS_OPTIONS = {
    1: {
        'DB': False,
        'SETTINGS': {}
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# this is an extremely simple Satchmo standalone store.

LOCAL_DEV = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.clowntown.me',
    '*'
]

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')

DIRNAME = os.path.dirname(os.path.abspath(__file__))

SATCHMO_DIRNAME = DIRNAME

def gettext_noop(string):
    """noop for gettext"""
    return string

LANGUAGES = (
    ('en', gettext_noop('English')),
)

# These are used when loading the test data
# SITE_NAME = "simple"

DATABASES = {
    'default': {
        # The last part of ENGINE is 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'ado_mssql'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ni',
        # Or path to database file if using sqlite3
        'USER': 'ni',  # Not used with sqlite3.
        'PASSWORD': 'pandas12',  # Not used with sqlite3.
        'HOST': 'ni.cogelwls8lwx.us-east-1.rds.amazonaws.com',
        # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',
        # Set to empty string for default. Not used with sqlite3.
    }
}

##### For Email ########
# If this isn't set in your settings file, you can set these here
# EMAIL_HOST = 'host here'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'your user here'
# EMAIL_HOST_PASSWORD = 'your password'
# EMAIL_USE_TLS = True

# These are used when loading the test data
SITE_DOMAIN = "ci.clowntown.me"
SITE_NAME = "ni ci"

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
# LOGFILE = "satchmo.log"
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#     datefmt='%a, %d %b %Y %H:%M:%S',
#     filename=os.path.join(DIRNAME, LOGFILE),
#     filemode='w'
# )
#
# logging.getLogger('django.db.backends').setLevel(logging.INFO)
# logging.getLogger('keyedcache').setLevel(logging.INFO)
# logging.getLogger('l10n').setLevel(logging.INFO)
# logging.getLogger('suds').setLevel(logging.INFO)
# logging.info("Satchmo Started")


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logstash': {
            'level': 'INFO',
            'class': 'logstash.TCPLogstashHandler',
            'host': 'ec2-52-7-147-163.compute-1.amazonaws.com',
            'port': 5959,  # Default value: 5959

            # Version of logstash event schema. Default value: 0 (for backward
            # compatibility of the library)
            'version': 1,

            # 'type' field in logstash message. Default value: 'logstash'
            # 'message_type': 'ni',

            # Fully qualified domain name. Default value: false
            # 'fqdn': False,

            # list of tags. Default: None.
            # 'tags': ['tag1', 'tag2'],
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['logstash'],
            'level': 'INFO',
            'propagate': True,
        },
        'ni': {
            'handlers': ['logstash'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
