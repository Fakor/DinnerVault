from django.views import View
from django.shortcuts import render

import json
from django.core.serializers.json import DjangoJSONEncoder

from main.models.plan import Plan, get_plans_after_today


class ViewMakePlans(View):
    template_name = 'main/make_plans.html'

    def get(self, request):
        plans = get_plans_after_today()
        p_json = json.dumps(plans, cls=DjangoJSONEncoder)
        context = {'plans': p_json}
        return render(request, self.template_name, context)
