"""
Base settings for local development.
TODO: use this for common settings
"""

import os
import sys

DIRNAME = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))
BASENAME = os.path.dirname(DIRNAME)

sys.path.append(os.path.join(BASENAME, 'satchmo'))

DJANGO_PROJECT = 'store'
DJANGO_SETTINGS_MODULE = 'ni.settings'

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

# Fixtures directory
FIXTURES_DIRS = (
    os.path.join(DIRNAME, 'fixtures/')
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
    # ... include the providers you want to enable:
    # '# allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.coinbase',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.dropbox_oauth2',
    # 'allauth.socialaccount.providers.evernote',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.fxa',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.odnoklassniki',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.spotify',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.xing',

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


ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# Load the local settings
# pylint: disable=wildcard-import, unused-wildcard-import
from ni.local_settings import *
