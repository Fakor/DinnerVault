from django.contrib import admin

from .models import *


class MealAdmin(admin.ModelAdmin):
    list_display = ['name']

class LabelAdmin(admin.ModelAdmin):
    list_display = ['text']

admin.site.register(Meal, MealAdmin)
admin.site.register(Label, LabelAdmin)
