from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder

import json
import datetime

from .models import *
from .forms import *


def index(request):
    return HttpResponse("Glufs!")


#@login_required
#def overview(request):
#    if request.method == 'POST':
#        if 'eaten_today' in request.POST:
#            meal = Meal.objects.get(id=request.POST['eaten_today'])
#            meal.add_date_today()
#        else:
#            return HttpResponse("Cant interpret post message!")
#    context = {'meals': order_meal_by_date(), 'labels': Label.objects.all()}
#    return render(request, 'main/overview.html', context)


# TODO Split this us so that adding a note and adding a date have different views and forms
@login_required
def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    form_values = {'date': datetime.date.today()}
    context = {'meal': meal}
    if request.method == 'POST':
        if 'submit_note' in request.POST:
            message = "New note"
            meal.add_note(request.POST.get('submit_note'))
        elif 'submit_date' in request.POST:
            date = request.POST.get('date_pick')
            year, month, day = [int(el) for el in date.split('-')]
            form_values['date'] = datetime.date(year, month, day)
            if meal.add_date(year, month, day):
                message = "Added date {}-{}-{}!".format(year, month, day)
            else:
                message = "Date {}-{}-{} is already added!".format(year, month, day)
        context['message'] = message
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
            post = request.POST
            meals=[]
            label = create_label_db(post['TEXT'], post['RED'], post['GREEN'], post['BLUE'])
            for value in request.POST.getlist('checked_meals'):
                meal = Meal.objects.get(id=int(value))
                meal.add_label(label)
                meals.append(meal)
            context = {'meals': meals, 'name': post['TEXT']}
            return render(request, 'main/label_created.html', context)
        else:
            return HttpResponse("Cant interpret post message!")
    context = {'meals': order_meal_by_date()}
    return render(request, 'main/create_label.html', context)

@login_required
def edit_label(request, label_id):
    label = get_object_or_404(Label, pk=label_id)
    if request.method == 'POST':
        post = request.POST
        label.text = post["TEXT"]
        label.color_red = post["RED"]
        label.color_green = post["GREEN"]
        label.color_blue = post["BLUE"]
        current_dinners = sort_meal_by_labels(required=[label])
        checked_dinners = set([int(el) for el in post.getlist("checked_meals")])
        for curr_din in current_dinners:
            if curr_din.id in checked_dinners:
                checked_dinners.remove(curr_din.id)
            else:
                curr_din.remove_label(label)
        for ch_din in checked_dinners:
            meal = get_object_or_404(Meal, pk=ch_din)
            meal.add_label(label)
        label.save()
    l_json = json.dumps(label.to_json(), cls=DjangoJSONEncoder)
    context = {'meals': order_meal_by_date(), 'label_json': l_json, "selected_meals": sort_meal_by_labels(required=[label])}
    return render(request, 'main/create_label.html', context)
