from django.db import models
import datetime


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
    recipe = models.CharField(max_length=1000, null=True)
    notes = models.ManyToManyField(Note)
    ingredients = models.ManyToManyField(Ingredient)
    dates = models.ManyToManyField(Date)
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

    def update_latest_date(self):
        self.latest_date = self.dates.order_by('date').reverse()[0].date
        self.save()

    def times_eaten(self):
        return self.dates.count()


def order_meal_by_date():
    return Meal.objects.order_by('latest_date')
