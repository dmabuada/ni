import logging

from django.db.models import Q
from django.contrib.sites.models import Site

from product.models import Category
from product.models import Product
from livesettings import config_value


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
    products = Product.objects.active_by_site(variations=False, site=site)

    price_range = query.get('price_range', None)
    if price_range:
        min_price, max_price = map(int, price_range.split('-'))
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


