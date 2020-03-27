from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from main.models import Meal, create_label_db, order_meal_by_date


class ViewCreateLabel(View):
    template_name = 'main/create_label.html'
    label_created_template = 'main/label_created.html'

    def get(self, request):
        context = {'meals': order_meal_by_date()}
        return render(request, self.template_name, context)

    def post(self, request):
        if 'create_label' in request.POST:
            post = request.POST
            meals=[]
            label = create_label_db(post['TEXT'], post['RED'], post['GREEN'], post['BLUE'])
            for value in request.POST.getlist('checked_meals'):
                meal = Meal.objects.get(id=int(value))
                meal.add_label(label)
                meals.append(meal)
            context = {'meals': meals, 'name': post['TEXT']}
            return render(request, self.label_created_template, context)
        else:
            return HttpResponse("Cant interpret post message!")
