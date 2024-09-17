# forms.py
from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')