from django.db import models
import datetime

from django.contrib.postgres.fields import ArrayField


class Classification(models.Model):
    name = models.CharField(max_length=10)


class Note(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, null=True)


class Date(models.Model):
    date = models.DateField()


class Meal(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(null=True)
    classification = models.ForeignKey(Classification, on_delete=models.PROTECT, null=False)
    recipe = models.CharField(max_length=1000, null=True)
    notes = models.ManyToManyField(Note)
    ingredients = models.ManyToManyField(Ingredient)
    dates = models.ManyToManyField(Date)

    def add_note(self, text):
        note = Note(text=text)
        note.save()
        self.notes.add(note)
        self.save()

    def add_date(self, year, month, day):
        date = Date(date=datetime.date(year, month, day))
        date.save()
        self.dates.add(date)
        self.save()
