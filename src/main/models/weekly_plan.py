from django.db import models

from main.models.dinner import Dinner


class WeeklyPlan(models.Model):
    monday_text = models.CharField(max_length=100, default="")
    monday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='monday')

    tuesday_text = models.CharField(max_length=100, default="")
    tuesday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='tuesday')

    wednesday_text = models.CharField(max_length=100, default="")
    wednesday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='wednesday')

    thursday_text = models.CharField(max_length=100, default="")
    thursday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='thursday')

    friday_text = models.CharField(max_length=100, default="")
    friday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='friday')

    saturday_text = models.CharField(max_length=100, default="")
    saturday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='saturday')

    sunday_text = models.CharField(max_length=100, default="")
    sunday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True, related_name='sunday')

    def to_json(self):
        return [
            {"day": "Monday", "dinner": self.monday_dinner, "text": self.monday_text},
            {"day": "Tuesday", "dinner": self.tuesday_dinner, "text": self.tuesday_text},
            {"day": "Wednesday", "dinner": self.wednesday_dinner, "text": self.wednesday_text},
            {"day": "Thursday", "dinner": self.thursday_dinner, "text": self.thursday_text},
            {"day": "Friday", "dinner": self.friday_dinner, "text": self.friday_text},
            {"day": "Saturday", "dinner": self.saturday_dinner, "text": self.saturday_text},
            {"day": "Sunday", "dinner": self.sunday_dinner, "text": self.sunday_text},
        ]