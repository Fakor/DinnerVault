from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

import datetime

from .models import Meal, order_meal_by_date, create_label_db
from .forms import *


def index(request):
    return HttpResponse("Glufs!")


@login_required
def overview(request):
    if request.method == 'POST':
        if 'eaten_today' in request.POST:
            meal = Meal.objects.get(id=request.POST['eaten_today'])
            meal.add_date_today()
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
        form = EditMealForm(request.POST)
        form_labels=LabelPickerForm(request.POST)
        if form.is_valid() and form_labels.is_valid():
            meal=form.save()
            form_labels.update_meal_with_labels(meal)
            return redirect('detail', meal_id=(form.instance.id))
        else:
            return HttpResponse("Failed creating meal!")
    else:
        form = EditMealForm()
        form_labels = LabelPickerForm()
        context = {'form': form, 'new': True, 'form_labels': form_labels}
        return render(request, 'main/edit_meal.html', context)

@login_required
def edit_meal(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    if request.method == 'POST':
        form=EditMealForm(request.POST)
        form_labels=LabelPickerForm(request.POST)
        if 'delete_dates' in request.POST:
            for date_id in request.POST.getlist('dates'):
                try:
                    d = meal.dates.filter(id=int(date_id))
                    d.delete()
                except:
                    pass
        elif form.is_valid() and form_labels.is_valid():
            form.update_meal(meal)
            form_labels.update_meal_with_labels(meal)
            return redirect('detail', meal_id=(meal.id))
    form = EditMealForm(instance=meal)
    form_labels = LabelPickerForm(labels=meal.labels)
    context = {'form': form, 'new': False, 'meal': meal, 'form_labels': form_labels, 'dates': meal.dates.all() }
    return render(request, 'main/edit_meal.html', context)

@login_required
def create_label(request):
    if request.method == 'POST':
        if 'create_label' in request.POST:
            form=LabelForm(request.POST)
            if form.is_valid():
                meals=[]
                label = create_label_db(form.cleaned_data['text'], form.cleaned_data['red'], form.cleaned_data['green'], form.cleaned_data['blue'])
                for value in request.POST.getlist('checked'):
                    meal = Meal.objects.get(id=int(value))
                    meal.add_label(label)
                    meals.append(meal)
                context = {'meals': meals, 'name': form.cleaned_data['text']}
                return render(request, 'main/label_created.html', context)
        else:
            return HttpResponse("Cant interpret post message!")
    form = LabelForm()
    context = {'meals': order_meal_by_date(), 'form': form}
    return render(request, 'main/create_label.html', context)

    