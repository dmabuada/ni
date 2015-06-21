"""
django app settings and signal binding
"""

from django.apps import AppConfig

from django.conf import settings

from ni.signals import store_search
from ni.listeners import product_search_listener
from ni.listeners import solr_search_listener


class NiAppConfig(AppConfig):
    """AppConfig for django"""
    name = 'ni'
    verbose_name = "Shops"

    def ready(self):
        if settings.USE_SOLR:
            store_search.connect(solr_search_listener)
        else:
            store_search.connect(product_search_listener)
