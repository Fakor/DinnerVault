from django import forms


class DetailForm(forms.Form):
    year = forms.IntegerField()
    month = forms.IntegerField()
    day = forms.IntegerField()
