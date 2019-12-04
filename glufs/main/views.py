from django.http import HttpResponse
from django.shortcuts import render

from .models import Meal


def index(request):
    return HttpResponse("Glufs!")


def overview(request):
    context={'meals': Meal.objects.all()}
    return render(request, 'main/overview.html', context)
