"""forms for ni"""

from django import forms

from product.models import Category
from product.models import Option


class SizeModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    """
    Class to override the label generator so that "size" shows up as `1'
    instead of `size: 1' or something
    """
    def label_from_instance(self, obj):
        return obj.value


class SearchForm(forms.Form):
    """The form that powers the search page"""
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

