from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View

import json
from django.core.serializers.json import DjangoJSONEncoder

from main.models import Meal, Label, order_meal_by_date, sort_meal_by_labels


class ViewEditLabel(View):
    template_name = 'main/create_label.html'

    def get(self, request, label_id):
        label = get_object_or_404(Label, pk=label_id)
        l_json = json.dumps(label.to_json(), cls=DjangoJSONEncoder)
        context = {'meals': order_meal_by_date(), 'label_json': l_json, "selected_meals": sort_meal_by_labels(required=[label])}
        return render(request, self.template_name, context)

    def post(self, request, label_id):
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
        context = {'meals': order_meal_by_date(), 'label_json': l_json,
                   "selected_meals": sort_meal_by_labels(required=[label])}
        return render(request, self.template_name, context)
