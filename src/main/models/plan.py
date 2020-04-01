from django.db import models

import datetime

from main.models.dinner import Dinner
from main.models.date import Date


class Plan(models.Model):
    text = models.CharField(max_length=50, null=True)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True)
    date = models.OneToOneField(Date, on_delete=models.CASCADE)


def get_plans_for_date(year, month, day):
    date = datetime.date(year, month, day)
    found_plans=[]
    for plan in Plan.objects.all():
        if plan.date.date == date:
            found_plans.append(plan)
    return found_plans


