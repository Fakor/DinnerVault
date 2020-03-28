from django import forms

from main.models.dinner import Dinner


class EditMealForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = ['name']

    def update_meal(self, meal):
        updated_meal = self.save(commit=False)
        meal.name = updated_meal.name
        meal.save()
