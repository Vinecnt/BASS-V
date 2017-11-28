# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 02:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taco', '0027_auto_20171127_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='ta',
            field=models.ManyToManyField(help_text='Select a TA for this course', to='taco.Ta'),
        ),
        migrations.AddField(
            model_name='courseupdate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taco.Course'),
        ),
        migrations.AddField(
            model_name='courseupdate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
