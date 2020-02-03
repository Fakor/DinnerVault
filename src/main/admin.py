from django.contrib import admin

from .models import Meal


class MealAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Meal, MealAdmin)
