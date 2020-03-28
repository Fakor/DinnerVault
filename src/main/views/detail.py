from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from main.models.dinner import Dinner


class ViewDetail(View):
    template_name='main/detail.html'

    submit_note = 'submit_note'
    submit_date = 'submit_date'

    def get(self, request, meal_id):
        meal = get_object_or_404(Dinner, pk=meal_id)
        context = {'meal': meal}
        return render(request, self.template_name, context)

    def post(self, request, meal_id):
        meal = get_object_or_404(Dinner, pk=meal_id)
        if self.submit_note in request.POST:
            message = "New note"
            meal.add_note(request.POST.get(self.submit_note))
        elif self.submit_date in request.POST:
            date = request.POST.get('date_pick')
            year, month, day = [int(el) for el in date.split('-')]
            if meal.add_date(year, month, day):
                message = "Added date {}-{}-{}!".format(year, month, day)
            else:
                message = "Date {}-{}-{} is already added!".format(year, month, day)
        context = {'meal': meal, 'message': message}
        return render(request, self.template_name, context)
