from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.sites.models import Site

from ni.forms import ShopForm
from ni.models import Shop

import logging

log = logging.getLogger('ni.views.create')


@login_required
def create_view(request, redirect=None, template="shop/create/new.html"):
    """
    Handle all shop creation logic.
    """

    form = ShopForm(request.POST)
    if request.method == 'POST' and form.is_valid():
            new_shop = Shop(
                name=form.cleaned_data['name'],
                owner=request.user,
                site=Site.objects.get_current()
                )
            new_shop.save()

            # look for explicit "next"
            next = request.POST.get('next', None)
            if not next:
                if redirect:
                    next = redirect
                else:
                    next = '/'
            return HttpResponseRedirect(next)

    form = ShopForm()
    context = RequestContext(request, {'form': form})

    return render_to_response(template, context_instance=context)
