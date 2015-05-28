"""
Takes a search form object and gathers results
"""

import logging

from django.db.models import Q
from django.contrib.sites.models import Site

from product.models import Category
from product.models import Product
from product.modules.configurable.models import ConfigurableProduct

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


    price_range = query.get('price_range', [])

    if price_range:
        q_list = []

        ranges = [i.split('-') for i in price_range]
        ranges = [(int(i), int(j)) for i, j in ranges]

        for lower, upper in ranges:
            q_list.append(Q(price__price__gte=lower) & Q(price__price__lte=upper))

        price_q = q_list.pop()

        for q in q_list:
            price_q = price_q | q

        products = products.filter(price_q)

    category_filter = query.get('category', [])
    if category_filter:
        products = products.filter(category__in=category_filter)

    # TODO: actually filter on size
    for keyword in keywords:
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
            sq.add(SQ(sizes=str(desired_size.value)), SQ.OR)

        sqs = sqs.filter(sq)

    keywords = query.get('q', '')
    if keywords:
        sqs = sqs.filter(text=keywords)

    category_filter = query.get('category', [])
    if category_filter:
        sq = SQ()

        for desired_category in category_filter:
            sq.add(SQ(categories=desired_category.name.lower()), SQ.OR)

        sqs = sqs.filter(sq)

    price_range = query.get('price_range', [])
    if price_range:
        sq = SQ()

        ranges = [i.split('-') for i in price_range]
        ranges = [(int(i), int(j)) for i, j in ranges]

        for lower, upper in ranges:
            sq.add(SQ(price__gte=lower) & SQ(price__lte=upper), SQ.OR)

        sqs = sqs.filter(sq)

    # TODO: don't return all, just return the queryset
    # which would mean it needs to be a generator that returns the object

    return [i.object for i in sqs.all()]

