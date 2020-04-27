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
            {"day": "Monday", "dinner": self.monday_dinner.id if self.monday_dinner else None, "text": self.monday_text},
            {"day": "Tuesday", "dinner": self.tuesday_dinner.id if self.tuesday_dinner else None, "text": self.tuesday_text},
            {"day": "Wednesday", "dinner": self.wednesday_dinner.id if self.wednesday_dinner else None, "text": self.wednesday_text},
            {"day": "Thursday", "dinner": self.thursday_dinner.id if self.thursday_dinner else None, "text": self.thursday_text},
            {"day": "Friday", "dinner": self.friday_dinner.id if self.friday_dinner else None, "text": self.friday_text},
            {"day": "Saturday", "dinner": self.saturday_dinner.id if self.saturday_dinner else None, "text": self.saturday_text},
            {"day": "Sunday", "dinner": self.sunday_dinner.id if self.sunday_dinner else None, "text": self.sunday_text},
        ]

    def get_dinner_form(self):
        return {
            "Monday_DINNER": self.monday_dinner,
            "Tuesday_DINNER": self.tuesday_dinner,
            "Wednesday_DINNER": self.wednesday_dinner,
            "Thursday_DINNER": self.thursday_dinner,
            "Friday_DINNER": self.friday_dinner,
            "Saturday_DINNER": self.saturday_dinner,
            "Sunday_DINNER": self.sunday_dinner,
        }