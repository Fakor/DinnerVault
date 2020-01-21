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


class Label(models.Model):
    text = models.CharField(max_length=20)
    color_red = models.IntegerField(default=100)
    color_green = models.IntegerField(default=100)
    color_blue = models.IntegerField(default=100)

    def get_color_string(self):
        return '#{:02X}{:02X}{:02X}'.format(self.color_red, self.color_green, self.color_blue)


class Meal(models.Model):
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

    def add_label(self, label):
        self.labels.add(label)
        self.save()


def order_meal_by_date():
    return Meal.objects.order_by('latest_date')

def create_label_db(text):
    label = Label(text=text)
    label.save()
    return label

def sort_meal_by_labels(required=[], excluded=[]):
    required_ids=[label.id for label in required]
    objects = Meal.objects.all()
    for req in required:
        objects = objects.filter(labels__in=[req])
    for excl in excluded:
        objects = objects.exclude(labels__in=[excl])
    return objects

def set_label_color(label, red, green, blue):
    label.red = red
    label.green = green
    label.blue = blue
    label.save()

