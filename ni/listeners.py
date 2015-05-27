"""
Takes a search form object and gathers results
"""

import logging

from django.db.models import Q
from django.contrib.sites.models import Site

from product.models import Category
from product.models import Product
from product.modules.configurable.models import ConfigurableProduct

from haystack.query import SearchQuerySet
# from livesettings import config_value

from haystack.query import SQ
from haystack.query import SearchQuerySet


# pylint: disable=unused-argument
def product_search_listener(sender, query, **kwargs):
    """
    TODO: just use a function call because this isn't the right way to use
    signals
    """
    log = logging.getLogger('search listener')

    keywords = query.get('k', '').split()
    sizes = query.get('size', None)

    log.debug('default product search listener')
    site = Site.objects.get_current()

    # show_pv = config_value('PRODUCT', 'SEARCH_SHOW_PRODUCTVARIATIONS', False)
    products = Product.objects.active_by_site(variations=False, site=site)

    price_range = query.get('price_range', None)
    if price_range:
        min_price, max_price = [int(i) for i in price_range.split('-')]
        products = products.filter(
            price__price__gt=min_price - 1,
            price__price__lt=max_price + 1
        )

    category = query.get('category', None)
    if category:
        categories = Category.objects.active(site=site, slug=category.slug)
        if categories:
            categories = categories[0].get_active_children(include_self=True)
        products = products.filter(category__in=categories)
    else:
        # automatically assumes active categories only
        categories = Category.objects.by_site(site=site)

    log.debug('initial: %s', list(products))

    # TODO: actually filter on size
    for keyword in keywords:
        if not category:
            categories = categories.filter(
                Q(name__icontains=keyword) |
                Q(meta__icontains=keyword) |
                Q(description__icontains=keyword)
            )

        products = products.filter(
            Q(name__icontains=keyword)
            | Q(short_description__icontains=keyword)
            | Q(description__icontains=keyword)
            | Q(meta__icontains=keyword)
            | Q(sku__iexact=keyword)
        )

    if sizes:
        variations = ConfigurableProduct.objects.filter(
            option_group__name='size').filter(product__in=products.all())
        products = [i.product for i in variations if i.get_product_from_options(
            sizes)]  # TODO: does this return parents

    return products


def solr_search_listener(sender, query, **kwargs):
    """
    search with solr
    """

    sqs = SearchQuerySet()

    size_filter = query.get('size', [])
    if size_filter:
        sq = SQ()

        for desired_size in size_filter:
            sq.add(SQ(sizes=desired_size), SQ.OR)

        sqs.filter(sq)

    keywords = query.get('q', '')
    if keywords:
        sqs = sqs.filter(text=keywords)

    # price_range = query.get('price_range', None)

    # TODO: don't return all, just return the queryset
    # which would mean it needs

    def return_obj(result_set):
        for result in result_set:
            yield result_set.object

    return [i.object for i in sqs.all()]

    # queryset = []
    #for result in SearchQuerySet().models(Product).filter((request.QUERY_PARAMS.get('q', ''))):
     #   queryset.append(result.object)
    #return queryset

