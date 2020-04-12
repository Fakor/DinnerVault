from django.views import View
from django.shortcuts import render
from django.core import serializers

import json


from main.models.plan import Plan
from main.models.dinner import order_dinner_by_date


class ViewMakePlans(View):
    template_name = 'main/make_plans.html'

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        plans = Plan.objects.all()
        p_json = serializers.serialize('json', plans)
        dinners = order_dinner_by_date()
        d_json = serializers.serialize('json', dinners, fields=('name'))

        return {'plans': p_json, 'dinners': d_json}
