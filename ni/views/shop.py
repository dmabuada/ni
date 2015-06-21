from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.paginator import Paginator

from ni.models import Shop


def shop_view(request, template="shop/search/shop.html"):
    """
    Perform a search based on keywords and categories in the form submission
    """

    if request.method == "GET" and request.GET.items():
        form = SearchForm(request.GET)
    else:
        form = SearchForm(request.POST)

    results = []

    if form.is_valid():
        res = store_search.send(Product, query=form.cleaned_data)
        # first listener tuple (0), response position (1, 0 is request)
        results = res[0][1]

    page = form.cleaned_data['page'] or 1
    context = RequestContext(request, {
        'page': Paginator(results, 20).page(page),
        'form': form
    })

    return render_to_response(template, context_instance=context)

