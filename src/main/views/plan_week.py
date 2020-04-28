from django.views import View
from django.shortcuts import render
from django.core import serializers

import json
from django.core.serializers.json import DjangoJSONEncoder

from main.models.weekly_plan import WeeklyPlan
from main.models.dinner import Dinner, order_dinner_by_date, get_dinner_or_none


class ViewPlanWeek(View):
    template_name='main/plan_week.html'

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request):
        p = request.POST
        w=self.get_week_plan()

        # Update dinners
        w.monday_dinner = get_dinner_or_none(p["Monday_DINNER"])
        w.tuesday_dinner = get_dinner_or_none(p["Tuesday_DINNER"])
        w.wednesday_dinner = get_dinner_or_none(p["Wednesday_DINNER"])
        w.thursday_dinner = get_dinner_or_none(p["Thursday_DINNER"])
        w.friday_dinner = get_dinner_or_none(p["Friday_DINNER"])
        w.saturday_dinner = get_dinner_or_none(p["Saturday_DINNER"])
        w.sunday_dinner = get_dinner_or_none(p["Sunday_DINNER"])

        # Update texts
        w.monday_text = p["Monday_TEXT"]
        w.tuesday_text = p["Tuesday_TEXT"]
        w.wednesday_text = p["Wednesday_TEXT"]
        w.thursday_text = p["Thursday_TEXT"]
        w.friday_text = p["Friday_TEXT"]
        w.saturday_text = p["Saturday_TEXT"]
        w.sunday_text = p["Sunday_TEXT"]

        w.save()
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        dinners = order_dinner_by_date()
        d_json = serializers.serialize('json', dinners, fields='name')
        weekly_plan = self.get_week_plan()
        w_json = json.dumps(weekly_plan.to_json(), cls=DjangoJSONEncoder)
        return {'dinners': d_json, 'week': w_json}

    def get_week_plan(self):
        weekly_plans = WeeklyPlan.objects.all()
        if weekly_plans.count() == 0:
            weekly_plan = WeeklyPlan()
            weekly_plan.save()
        else:
            weekly_plan = weekly_plans[0]
        return weekly_plan
