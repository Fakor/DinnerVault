from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Meal


def index(request):
    return HttpResponse("Glufs!")


def overview(request):
    context={'meals': Meal.objects.all()}
    return render(request, 'main/overview.html', context)


def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    context={'meal': meal}
    return render(request, 'main/detail.html', context)
