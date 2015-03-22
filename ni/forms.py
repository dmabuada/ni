from django import forms
from product.models import Category


class SearchForm(forms.Form):
    k = forms.CharField(label='', max_length=100, required=False)
    category = forms.ModelChoiceField(Category.objects.all(), required=False)
