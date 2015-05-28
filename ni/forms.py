"""forms for ni"""

from django import forms

from product.models import Category
from product.models import Option
from product.models import Product

class OverrideMultipleLabel(forms.ModelMultipleChoiceField):
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

    size = OverrideMultipleLabel(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Option.objects.filter(option_group__name='size').all(),
    )

    color = forms.ModelMultipleChoiceField(
        queryset=Product.objects.filter(total_sold=0).all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
