from django import forms

from .models import Label, Meal


class ColorField(forms.IntegerField):

    def validate(self, value):
        super().validate(value)
        if value < 0 or value > 255:
            forms.ValidationError( ('Invalid value'), code='invalid')


class DetailForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(), required=False)
    new_note = forms.CharField(required=False)


class EditMealForm(forms.Form):
    name = forms.CharField()

    def __init__(self, *args, meal=None, **kwargs):
        initial = {}
        if meal is not None:
            initial['name']=meal.name
        super(EditMealForm, self).__init__(*args, initial=initial, **kwargs)
        for l in Label.objects.all():
            label_name=l.text
            self.fields[label_name]=forms.BooleanField(required=False)
 

class LabelForm(forms.Form):
    text = forms.CharField(max_length=Label._meta.get_field('text').max_length)
    red = ColorField()
    green= ColorField()
    blue = ColorField()


