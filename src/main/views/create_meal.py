from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.forms import EditMealForm, LabelPickerForm


class ViewCreateMeal(View):
    template_name = 'main/edit_meal.html'
    detail_name = 'detail'

    def get(self, request):
        form = EditMealForm()
        form_labels = LabelPickerForm()
        context = {'form': form, 'new': True, 'form_labels': form_labels}
        return render(request, self.template_name, context)

    def post(self, request):
        form = EditMealForm(request.POST)
        form_labels = LabelPickerForm(request.POST)
        if form.is_valid() and form_labels.is_valid():
            meal=form.save()
            form_labels.update_meal_with_labels(meal)
            return redirect(self.detail_name, meal_id=form.instance.id)
        else:
            return HttpResponse("Failed creating meal!")
