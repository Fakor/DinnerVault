from django.db import models

import datetime

from main.models.dinner import Dinner


class Plan(models.Model):
    text = models.CharField(max_length=50, null=True)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True)
    date = models.DateField()


def get_plans_for_date(year, month, day):
    date = datetime.date(year, month, day)
    found_plans=[]
    for plan in Plan.objects.all():
        if plan.date == date:
            found_plans.append(plan)
    return found_plans


def get_plans_after_date(year, month, day):
    date = datetime.date(year, month, day)
    found_plans=[]
    for plan in Plan.objects.order_by('date'):
        if plan.date >= date:
            found_plans.append(plan)
    return found_plans
