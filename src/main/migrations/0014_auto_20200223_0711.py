# Generated by Django 3.0.2 on 2020-02-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200221_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='text',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
