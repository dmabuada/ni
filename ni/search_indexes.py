"""
solr index configuration
"""

import datetime
from django.contrib.sites.models import Site

from haystack import indexes

from product.models import Product
from product.modules.configurable.models import ConfigurableProduct
from ni.configuration import get_colors

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    """
    index for the Product model
    """

    # text = indexes.CharField(document=True, use_template=True)
    # author = indexes.CharField(model_attr='user')
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    date_added = indexes.DateTimeField(model_attr='date_added')

    colors = indexes.MultiValueField()
    sizes = indexes.MultiValueField()

    def prepare_sizes(self, obj):
        configured = ConfigurableProduct.objects.filter(option_group__name='size').filter(product=obj).first()
        if configured is None:
            return []
        return [int(i[0].value) for i in configured.get_all_options()]

    def prepare_colors(self, obj):
        image_path = obj.main_image.picture.path
        return get_colors.colorz(image_path, n=3)

    categories = indexes.MultiValueField()

    def prepare_categories(self, obj):
        return [category.name.lower() for category in obj.category.all()]

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""

        site = Site.objects.get_current()

        product = self.get_model()
        products = product.objects.active_by_site(variations=False, site=site)

        return products.filter(date_added__lte=datetime.datetime.now())
