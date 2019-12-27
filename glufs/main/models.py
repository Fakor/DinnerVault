from django.db import models


class Classification(models.Model):
    name = models.CharField(max_length=10)


class Note(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20, null=True)


class Meal(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(null=True)
    classification = models.ForeignKey(Classification, on_delete=models.PROTECT, null=False)
    recipe = models.CharField(max_length=1000, null=True)
    notes = models.ManyToManyField(Note)
    ingredients = models.ManyToManyField(Ingredient)

    def add_note(self, text):
        note = Note(text=text)
        note.save()
        self.notes.add(note)
        self.save()
