from django.db import models

from main.models.dinner import Dinner


class Plan(models.Model):
    text = models.CharField(max_length=200, null=True)
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
