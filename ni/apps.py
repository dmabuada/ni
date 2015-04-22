from django.apps import AppConfig

from signals import store_search
from listeners import product_search_listener


class NiAppConfig(AppConfig):
    name = 'ni'
    verbose_name = "ni still"

    def ready(self):
        store_search.connect(product_search_listener)
