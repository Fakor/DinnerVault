from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(null=True)
