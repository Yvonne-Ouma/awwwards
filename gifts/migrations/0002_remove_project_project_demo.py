# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_demo',
        ),
    ]
