# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.TextField(unique=True),
        ),
    ]
