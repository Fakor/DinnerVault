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


class EditMealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name']

    label_pattern='__LABEL__'

    def __init__(self, *args, **kwargs):
        super(EditMealForm, self).__init__(*args, **kwargs)
        for l in Label.objects.all():
            label_name='{}{}'.format(self.label_pattern, l.text)
            self.fields[label_name]=forms.BooleanField(required=False)
            try:
                self.fields[label_name].initial=self.instance.have_label(l)
            except ValueError:
                pass

    def update_meal(self, meal):
        updated_meal = self.save(commit=False)
        meal.name = updated_meal.name
        meal.save()

class LabelForm(forms.Form):
    text = forms.CharField(max_length=Label._meta.get_field('text').max_length)
    red = ColorField()
    green= ColorField()
    blue = ColorField()


