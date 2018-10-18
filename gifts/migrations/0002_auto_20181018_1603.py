# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('design', models.IntegerField(choices=[(6, '6'), (10, '10'), (9, '9'), (8, '8'), (4, '4'), (3, '3'), (2, '2'), (7, '7'), (5, '5'), (1, '1')], default=0)),
                ('usability', models.IntegerField(choices=[(6, '6'), (10, '10'), (9, '9'), (8, '8'), (4, '4'), (3, '3'), (2, '2'), (7, '7'), (5, '5'), (1, '1')], default=0)),
                ('content', models.IntegerField(choices=[(6, '6'), (10, '10'), (9, '9'), (8, '8'), (4, '4'), (3, '3'), (2, '2'), (7, '7'), (5, '5'), (1, '1')], default=0)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gifts.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='votes',
            name='project',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='user',
        ),
        migrations.DeleteModel(
            name='Votes',
        ),
    ]