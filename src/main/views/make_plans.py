from django.views import View
from django.shortcuts import render
from django.core import serializers

from main.models.plan import Plan
from main.models.dinner import Dinner, order_dinner_by_date


class ViewMakePlans(View):
    template_name = 'main/make_plans.html'

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request):
        p = request.POST
        if "NEW_NAME" in p:
            names = p.getlist('NEW_NAME', default=[])
            dinners = p.getlist('NEW_DINNER', default=[])
            texts = p.getlist('NEW_TEXT', default=[])
            print(names, dinners, texts)
            for name, dinner_id, text in zip(names, dinners, texts):
                if not name and not dinner_id and not text:
                    continue
                if dinner_id:
                    dinner = Dinner.objects.get(id=int(dinner_id))
                else:
                    dinner = None
                new_plan=Plan(name=name, dinner=dinner, text=text)
                new_plan.save()
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        plans = Plan.objects.all()
        p_json = serializers.serialize('json', plans)
        dinners = order_dinner_by_date()
        d_json = serializers.serialize('json', dinners, fields=('name'))

        return {'plans': p_json, 'dinners': d_json}
