# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-08 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0036_auto_20171208_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='assignment_link',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='tid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Ta'),
        ),
        migrations.AlterField(
            model_name='course',
            name='ta',
            field=models.ManyToManyField(help_text='Select a TA for this course', to='taco.Ta'),
        ),
    ]
