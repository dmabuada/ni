from django import forms
from product.models import Category
from product.models import Option


class SearchForm(forms.Form):
    k = forms.CharField(label='', max_length=100, required=False)
    category = forms.ModelChoiceField(Category.objects.all(), required=False)

    size = forms.ModelChoiceField(
        Option.objects.values_list('name', flat=True).distinct(),
        required=False
    )
