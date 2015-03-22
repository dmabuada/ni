from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import Product
from satchmo_utils.signals import application_search
from ni.forms import SearchForm
from ni.signals import store_search


def search_view(request, template="shop/search2.html"):
    """
    Perform a search based on keywords and categories in the form submission
    """

    if request.method == "GET":
        form = SearchForm(request.GET)
    else:
        form = SearchForm(request.POST)

    results = {}

    if form.is_valid():
        res = store_search.send(Product, query=form.cleaned_data)
        # first listener tuple (0), response position (1, 0 is request)
        results = res[0][1]

    context = RequestContext(request, {
        'results': results,
        'form': form
    })

    return render_to_response(template, context_instance=context)
