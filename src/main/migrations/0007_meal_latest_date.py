# Generated by Django 2.2.7 on 2019-12-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_meal_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='latest_date',
            field=models.DateField(null=True),
        ),
    ]
