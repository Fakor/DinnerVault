from django.contrib import admin

from main.models.dinner import Dinner
from main.models.label import Label


class MealAdmin(admin.ModelAdmin):
    list_display = ['name']


class LabelAdmin(admin.ModelAdmin):
    list_display = ['text']


admin.site.register(Dinner, MealAdmin)
admin.site.register(Label, LabelAdmin)
