# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-26 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voley', '0003_auto_20160625_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posicion',
            old_name='pe',
            new_name='ppa0',
        ),
        migrations.RenameField(
            model_name='posicion',
            old_name='pp',
            new_name='ppa1',
        ),
        migrations.AddField(
            model_name='posicion',
            name='coefSet',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posicion',
            name='puntos',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
