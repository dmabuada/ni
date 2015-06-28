from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.shortcuts import render_to_response


from ni.forms import ShopForm
from ni.models import Shop

from django.contrib.sites.models import Site


def create_view(request, redirect=None, template="shop/create/new.html"):
    """
    Handle all shop creation logic.
    """

    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
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
    context = RequestContext(request)

    return render_to_response(template, {'form': form}, context_instance=context)
