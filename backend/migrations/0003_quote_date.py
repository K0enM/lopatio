# Generated by Django 3.1.1 on 2020-09-21 23:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200922_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
