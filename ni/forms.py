"""forms for ni"""

import math

from django import forms
from django.db.models import Min, Max
from django.db.utils import OperationalError

from product.models import Category
from product.models import Option
from product.models import Price


class SizeModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """
    Class to override the label generator so that "size" shows up as `1'
    instead of `size: 1' or something
    """

    def label_from_instance(self, obj):
        return obj.value


class CategoryModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """
    Class to override the label generator so that "category" shows up as
    'Formal dresses' instead of 'Dresses :: Formal dresses'
    """

    def label_from_instance(self, obj):
        return obj.name


def price_range_choices():
    try:
        min_price = Price.objects.all().aggregate(Min('price'))['price__min'] or 0
        max_price = Price.objects.all().aggregate(Max('price'))['price__max'] or 8
    except OperationalError as oe:
        # The table isn't created yet. Okay if doing first migration
        return []

    price_range = max_price - min_price
    step_size = int(math.ceil(price_range / 4))

    ranges = [(i, (i + step_size) - 1) for i in
              range(min_price, max_price, step_size)]
    return [('{}-{}'.format(*i), '${}-${}'.format(*i)) for i in ranges]


class SearchForm(forms.Form):
    """The form that powers the search page"""
    q = forms.CharField(widget=forms.HiddenInput(), required=False)

    page = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    category = CategoryModelMultipleChoiceField(
        queryset=Category.objects.filter(parent__name='Dresses').all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    start_date = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'delivery-date'}),
        required=False
    )

    end_date = forms.CharField(
        widget=forms.TextInput({'id': 'return-date'}),
        required=False
    )

    size = SizeModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Option.objects.filter(option_group__name='size').all(),
    )

    price_range = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        choices=price_range_choices(),
    )
