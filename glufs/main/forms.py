from django import forms


class DetailForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())
