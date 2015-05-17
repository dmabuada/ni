import math

from django import forms
from django.db.models import Min, Max

from product.models import Category
from product.models import Option
from product.models import Price


# TODO: use the one from the homepage correctly
# from django.forms.extras.widgets import SelectDateWidget


class SizeModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.value


class SearchForm(forms.Form):
    occasion = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    category = forms.ModelChoiceField(Category.objects.all(), required=False)

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

