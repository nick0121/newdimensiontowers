# Generated by Django 3.0.3 on 2020-03-25 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200318_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='url-slug'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('tower', 'Tower'), ('bimini', 'Bimini'), ('gear', 'Gear'), ('board-racks', 'Board Racks'), ('accessory', 'Accessory')], default='accessory', max_length=50, verbose_name='Category'),
        ),
    ]
