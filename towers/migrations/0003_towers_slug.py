# Generated by Django 3.0.3 on 2020-03-25 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towers', '0002_auto_20200318_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='towers',
            name='slug',
            field=models.SlugField(default='this-is-a-slug'),
        ),
    ]