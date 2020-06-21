from django.views import View
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from main.models.dinner import Dinner
from main.forms.edit_meal import EditMealForm
from main.forms.label_picker import LabelPickerForm


class ViewEditMeal(View):
    template_name='main/edit_meal.html'
    detail_name = 'detail'

    def get(self, request, meal_id):
        return render(request, self.template_name, self.get_context(meal_id))

    def post(self, request, meal_id):
        meal = get_object_or_404(Dinner, pk=meal_id)
        form = EditMealForm(request.POST)
        form_labels = LabelPickerForm(request.POST)
        if 'delete_dates' in request.POST:
            for date_id in request.POST.getlist('dates'):
                d = meal.dates.filter(id=int(date_id))
                d.delete()
                meal.update_latest_date()
        elif form.is_valid() and form_labels.is_valid():
            form.update_meal(meal)
            form_labels.update_meal_with_labels(meal)
            meal.info = request.POST['submit_info'].strip()
            meal.save()
            return redirect(self.detail_name, meal_id=meal.id)
        return render(request, self.template_name, self.get_context(meal_id))

    def get_context(self, meal_id):
        meal = get_object_or_404(Dinner, pk=meal_id)
        form = EditMealForm(instance=meal)
        form_labels = LabelPickerForm(labels=meal.labels)

        return {'form': form,
                'new': False,
                'meal': meal,
                'form_labels': form_labels,
                'dates': meal.dates.all() }
