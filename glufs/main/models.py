from django.db import models


class Meal(models.Model):
    name_text = models.CharField(max_length=50)
