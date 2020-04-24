from django.views import View
from django.shortcuts import render
from django.core import serializers

from main.models.weekly_plan import WeeklyPlan
from main.models.dinner import Dinner, order_dinner_by_date


class ViewPlanWeek(View):
    template_name='main/plan_week.html'

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        dinners = order_dinner_by_date()
        d_json = serializers.serialize('json', dinners, fields='name')
        weekly_plans = WeeklyPlan.objects.all()
        if weekly_plans.count() == 0:
            weekly_plan = WeeklyPlan()
            weekly_plan.save()
        else:
            weekly_plan = weekly_plans[0]
        return {'dinners': d_json, 'week': weekly_plan}