from django import forms
from product.models import Category
from product.models import Option

from django.db.models import Min, Max
from product.models import Price

import math

# TODO: use the one from the homepage correctly
# from django.forms.extras.widgets import SelectDateWidget


def _prices():
    min_price = Price.objects.all().aggregate(Min('price'))['price__min']
    max_price = Price.objects.all().aggregate(Max('price'))['price__max']

    price_range = max_price - min_price
    step_size = int(math.ceil(price_range / 4))

    r = []
    for i in range(min_price, max_price, step_size):
        r.append((i, (i + step_size) - 1))
    return r


# class DateRangeSelectWidget(forms.TextInput):
#     def render(self, name, value, attrs=None):
#         return super(DateRangeSelectWidget, self).render(
#             self, name, value, attrs
#         )


class SearchForm(forms.Form):
    k = forms.CharField(label='', max_length=100, required=False)
    category = forms.ModelChoiceField(Category.objects.all(), required=False)

    start_date = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'delivery-date'}),
        required=False
    )

    end_date = forms.CharField(
        widget=forms.TextInput({'id': 'return-date'}),
        required=False
    )


    size = forms.ModelChoiceField(
        Option.objects.values_list('name', flat=True).distinct(),
        required=False,
        widget=forms.RadioSelect
    )

    price_range = forms.ChoiceField(
        [('{}-{}'.format(*i), '${}-${}'.format(*i)) for i in _prices()],
        required=False,
        widget=forms.RadioSelect
    )
