# Generated by Django 4.0.5 on 2022-06-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voltlines_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='registered_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
