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

    def update_meal(self, meal):
        updated_meal = self.save(commit=False)
        meal.name = updated_meal.name
        meal.save()


class LabelPickerForm(forms.Form):

    def __init__(self, *args, **kwargs):
        labels = kwargs.pop('labels', None)
        super(LabelPickerForm, self).__init__(*args, **kwargs)
        for l in Label.objects.all():
            if labels:
                default=l in labels.all()
            else:
                default=False
            self.fields[l.text] = forms.BooleanField(required=False)
            self.fields[l.text].initial = default

    def update_meal_with_labels(self, meal):
        meal.labels.clear()
        for key, label in self.fields.items():
            if self.cleaned_data[key]:
                try:
                    meal.add_label(Label.objects.filter(text=key)[0])
                except:
                    pass

class LabelForm(forms.Form):
    text = forms.CharField(max_length=Label._meta.get_field('text').max_length)
    red = ColorField()
    green= ColorField()
    blue = ColorField()

