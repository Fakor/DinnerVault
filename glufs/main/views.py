from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Meal, order_meal_by_date
from .forms import DetailForm

def index(request):
    return HttpResponse("Glufs!")


def overview(request):
    context={'meals': order_meal_by_date()}
    return render(request, 'main/overview.html', context)


def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            year = int(request.POST.get('year'))
            month = int(request.POST.get('month'))
            day = int(request.POST.get('day'))
            meal.add_date(int(year), int(month), int(day))
            return HttpResponse("Added date!")
        else:
            return HttpResponse("Failed adding date!")
    else:
        form = DetailForm()
        context={'meal': meal, 'form': form}
        return render(request, 'main/detail.html', context)
