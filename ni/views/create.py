from django.http import HttpResponseRedirect
from django.core import urlresolvers
from django.template import RequestContext

from django.shortcuts import render_to_response


from ni.forms import ShopForm
from ni.models import Shop


def create_view(request, redirect=None, template="shop/create/new.html"):
    """
    Handle all shop creation logic.
    """

    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(request, force_new=True)

            # look for explicit "next"
            next = request.POST.get('next', None)
            if not next:
                if redirect:
                    next = redirect
                else:
                    next = urlresolvers.reverse('shop_creation_complete')
            return HttpResponseRedirect(next)

    else:
        initial_data = {}
        try:
            shop = Shop.objects.all()[0]
            initial_data = {
                'shop': shop.name
            }
        except Shop.DoesNotExist:
            #log here for debugging
            shop = None

        initial_data['next'] = request.GET.get('next', '')

        form = ShopForm(initial=initial_data)
        context = RequestContext(request)

    return render_to_response(template, {'form': form}, context_instance=context)
