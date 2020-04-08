from django.views import View
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

import json


from main.models.plan import Plan, get_plans_after_today
from main.models.dinner import order_dinner_by_date


class ViewMakePlans(View):
    template_name = 'main/make_plans.html'

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        plans = get_plans_after_today()
        p_json = json.dumps(plans, cls=DjangoJSONEncoder)
        dinners = order_dinner_by_date()
        d_json = serializers.serialize('json', dinners)
        return {'plans': p_json, 'dinners': d_json}
