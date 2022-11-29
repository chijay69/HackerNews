from django import forms


# form goes here
class SearchForm(forms.Form):
    query = forms.CharField(max_length=250)
