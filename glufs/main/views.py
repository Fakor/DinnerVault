from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

import datetime

from .models import Meal, order_meal_by_date
from .forms import DetailForm, EditForm


def index(request):
    return HttpResponse("Glufs!")


@login_required
def overview(request):
    if request.method == 'POST':
        if 'create_meal' in request.POST:
            return redirect('create_meal')
        elif 'logout' in request.POST:
            return redirect('logout')
        else:
            return HttpResponse("Cant interpret post message!")
    context = {'meals': order_meal_by_date()}
    return render(request, 'main/overview.html', context)


# TODO Split this us so that adding a note and adding a date have different views and forms
@login_required
def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    form_values = {'date': datetime.date.today()}
    context = {'meal': meal}
    if request.method == 'POST':
        form_post = DetailForm(request.POST)
        if form_post.is_valid():
            if 'submit_note' in request.POST:
                message = "Ny notering"
                meal.add_note(request.POST.get('new_note'))
            elif 'submit_date' in request.POST:
                year = int(request.POST.get('date_year'))
                month = int(request.POST.get('date_month'))
                day = int(request.POST.get('date_day'))
                form_values['date'] = datetime.date(year, month, day)
                if meal.add_date(year, month, day):
                    message = "Lade till datum {}-{}-{}!".format(year, month, day)
                else:
                    message = "Datum {}-{}-{} tillagd sen tidigare!".format(year, month, day)
        else:
            message = "Failed adding date!"
        context['message'] = message
    form = DetailForm(initial=form_values)
    context['form'] = form
    return render(request, 'main/detail.html', context)


@login_required
def create_meal(request):
    if request.method == 'POST':
        form_post = EditForm(request.POST)
        if form_post.is_valid():
            name = request.POST.get('name')
            meal = Meal(name=name)
            meal.save()
            return redirect('detail', meal_id=(meal.id))
        else:
            return HttpResponse("Failed creating meal!")
    else:
        form = EditForm()
        context = {'form': form}
        return render(request, 'main/edit_meal.html', context)
