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
        self.label_fields={}
        self.label_init_active=[]
        for l in Label.objects.all():
            label_name='{}{}'.format(self.label_pattern, l.text)
            self.fields[label_name]=forms.BooleanField(required=False)
            self.label_fields[label_name]=l
            try:
                self.fields[label_name].initial=self.instance.have_label(l)
                if self.fields[label_name].initial:
                    self.label_init_active.append(label_name)
            except ValueError:
                pass
        self.selected_labels=[]

    def save(self, commit=True):
        m = super(EditMealForm, self).save(commit=False)
        self.new_labels = []
        for key, label in self.label_fields.items():
            if self.cleaned_data[key]:
                self.new_labels.append(label)
        if commit:
            m.save()
            self.update_labels(m)
        return m

    def update_labels(self, meal):
        meal.labels.clear()
        for label in self.new_labels:
            meal.labels.add(label)
        meal.save()

    def update_meal(self, meal):
        updated_meal = self.save(commit=False)
        meal.name = updated_meal.name
        self.update_labels(meal)


class LabelForm(forms.Form):
    text = forms.CharField(max_length=Label._meta.get_field('text').max_length)
    red = ColorField()
    green= ColorField()
    blue = ColorField()


