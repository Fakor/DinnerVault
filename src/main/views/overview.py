from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from main.models.dinner import Dinner, order_dinner_by_date
from main.models.label import Label


class ViewOverview(View):
    template_name = 'main/overview.html'

    def get(self, request):
        return render(request, self.template_name, self.get_context())

    def post(self, request):
        if 'eaten_today' in request.POST:
            meal = Dinner.objects.get(id=request.POST['eaten_today'])
            meal.add_date_today()
        else:
            return HttpResponse("Cant interpret post message!")
        return render(request, self.template_name, self.get_context())

    def get_context(self):
        return {'meals': order_dinner_by_date(), 'labels': Label.objects.all()}

