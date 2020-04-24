from django.db import models

from main.models.dinner import Dinner


class WeeklyPlan(models.Model):
    monday_text = models.CharField(max_length=100, null=True)
    monday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='monday')

    tuesday_text = models.CharField(max_length=100, null=True)
    tuesday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='tuesday')

    wednesday_text = models.CharField(max_length=100, null=True)
    wednesday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='wednesday')

    thursday_text = models.CharField(max_length=100, null=True)
    thursday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='thursday')

    friday_text = models.CharField(max_length=100, null=True)
    friday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='friday')

    saturday_text = models.CharField(max_length=100, null=True)
    saturday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='saturday')

    sunday_text = models.CharField(max_length=100, null=True)
    sunday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='sunday')

