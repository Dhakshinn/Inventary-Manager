# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-11 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20181010_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='image',
        ),
    ]