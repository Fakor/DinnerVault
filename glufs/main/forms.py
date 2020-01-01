from django import forms


class DetailForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(), required=False)
    new_note = forms.CharField(required=False)
