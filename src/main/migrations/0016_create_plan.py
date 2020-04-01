from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0015_auto_20200328_2036')
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, null=True))
            ]
        )

    ]
