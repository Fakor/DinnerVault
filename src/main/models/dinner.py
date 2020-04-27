from django.db import models

import datetime

from main.models.label import Label
from main.models.date import Date
from main.models.ingredient import Ingredient
from main.models.note import Note


class Dinner(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.CharField(max_length=1000, null=True)
    notes = models.ManyToManyField(Note)
    ingredients = models.ManyToManyField(Ingredient)
    dates = models.ManyToManyField(Date)
    labels = models.ManyToManyField(Label)
    latest_date = models.DateField(default=datetime.date(1, 1, 1))

    def add_note(self, text):
        note = Note(text=text)
        note.save()
        self.notes.add(note)
        self.save()

    def add_date(self, year, month, day):
        d = datetime.date(year, month, day)
        if self.dates.filter(date=d):
            return False
        date = Date(date=d)
        date.save()
        self.dates.add(date)
        self.save()
        self.update_latest_date()
        return True

    def add_date_today(self):
        now = datetime.date.today()
        self.add_date(now.year, now.month, now.day)

    def update_latest_date(self):
        self.latest_date = self.dates.order_by('date').reverse()[0].date
        self.save()

    def times_eaten(self):
        return self.dates.count()

    def add_label(self, label, commit=True):
        self.labels.add(label)
        if commit:
            self.save()

    def remove_label(self, label, commit=True):
        self.labels.remove(label)
        if commit:
            self.save()

    def have_label(self, label):
        return len(self.labels.filter(id__in=[label.id])) > 0


def get_dinner_or_none(dinner_id):
    if dinner_id:
        return Dinner.objects.get(id=int(dinner_id))
    return None


def order_dinner_by_date():
    return Dinner.objects.order_by('latest_date')


def sort_dinners_by_labels(required=[], excluded=[]):
    objects = Dinner.objects.all()
    for req in required:
        objects = objects.filter(labels__in=[req])
    for excl in excluded:
        objects = objects.exclude(labels__in=[excl])
    return objects
