# Generated by Django 2.2.7 on 2019-12-29 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_meal_latest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='latest_date',
            field=models.DateField(default=datetime.date(1, 1, 1)),
        ),
    ]
