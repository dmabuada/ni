"""
django app settings and signal binding
"""

from django.apps import AppConfig

from ni.signals import store_search
from ni.listeners import product_search_listener


class NiAppConfig(AppConfig):
    """AppConfig for django"""
    name = 'ni'
    verbose_name = "ni still"

    def ready(self):
        store_search.connect(product_search_listener)
