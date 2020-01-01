from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

import datetime

from .models import Meal, order_meal_by_date
from .forms import DetailForm


def index(request):
    return HttpResponse("Glufs!")


def overview(request):
    context = {'meals': order_meal_by_date()}
    return render(request, 'main/overview.html', context)


def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            year = int(request.POST.get('date_year'))
            month = int(request.POST.get('date_month'))
            day = int(request.POST.get('date_day'))
            form = DetailForm(initial={'date': datetime.date(year, month, day)})
            if 'submit_date' in request.POST:
                if meal.add_date(year, month, day):
                    message = "Lade till datum {}-{}-{}!".format(year, month, day)
                else:
                    message = "Datum {}-{}-{} tillagd sen tidigare!".format(year, month, day)
            elif 'submit_note':
                message = "Ny notering"
                meal.add_note(request.POST.get('new_note'))
        else:
            now = datetime.date.today()
            form = DetailForm(initial={'date': now})
            message = "Failed adding date!"
        context = {'meal': meal, 'form': form, 'message': message}
    else:
        now = datetime.date.today()
        form = DetailForm(initial={'date': now})
        context={'meal': meal, 'form': form}
    return render(request, 'main/detail.html', context)
