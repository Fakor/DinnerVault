from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from main.models import Meal, order_meal_by_date, Label


class ViewOverview(View):
    template_name = 'main/overview.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context())

    def post(self, request, *args, **kwargs):
        if 'eaten_today' in request.POST:
            meal = Meal.objects.get(id=request.POST['eaten_today'])
            meal.add_date_today()
        else:
            return HttpResponse("Cant interpret post message!")
        return render(request, self.template_name, self.get_context())

    def get_context(self):
        return {'meals': order_meal_by_date(), 'labels': Label.objects.all()}

