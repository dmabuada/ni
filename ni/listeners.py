from product.models import Category
from product.models import Product, OptionGroup
from product.modules.configurable.models import ProductVariation
from django.db.models import Q
from django.contrib.sites.models import Site
from livesettings import config_value

from product.models import Option

import logging

log = logging.getLogger('search listener')


def product_search_listener(sender, query, **kwargs):
    """
    TODO: just use a function call because this isn't the right way to use
    signals
    """

    keywords = query.get('k', '').split()
    size = query.get('size', None)

    log.debug('default product search listener')
    site = Site.objects.get_current()

    show_pv = config_value('PRODUCT', 'SEARCH_SHOW_PRODUCTVARIATIONS', False)

    products = Product.objects.active_by_site(variations=show_pv, site=site)

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

    if size:
        # size_options = OptionGroup.objects.filter(name='size')
        # products = products.filter(
        #     Q(option_group__name='size')
        # )
        pass

    return {
        'categories': categories,
        'products': products
    }


