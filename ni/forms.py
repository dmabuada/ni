from django import forms
from product.models import Category
from product.models import Option


# TODO: use the one from the homepage correctly
from django.forms.extras.widgets import SelectDateWidget


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
        required=False
    )
