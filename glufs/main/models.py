from django.db import models


class Classification(models.Model):
    name = models.CharField(max_length=10)


class Meal(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(null=True)
    classification = models.ForeignKey(Classification, on_delete=models.PROTECT, null=False)
