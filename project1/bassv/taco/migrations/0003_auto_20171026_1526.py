# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taco', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('aid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the Assignment', primary_key=True, serialize=False)),
                ('assignment_link', models.CharField(help_text='Enter the link to find the Assignment', max_length=200)),
                ('aname', models.CharField(help_text='Entera name for the Assignment', max_length=200)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Course')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Course')),
            ],
        ),
        migrations.CreateModel(
            name='MessageCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Message')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the Professor', primary_key=True, serialize=False)),
                ('pname', models.CharField(help_text="Enter Professor's Name", max_length=200)),
                ('courseOfferingID', models.ManyToManyField(help_text='Select a course by this Professor', to='taco.Course')),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('tid', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the TA', primary_key=True, serialize=False)),
                ('tname', models.CharField(help_text='Enter First Name', max_length=200)),
                ('courseOfferingID', models.ManyToManyField(help_text='Select a course assigned to TA', to='taco.Course')),
            ],
        ),
        migrations.AddField(
            model_name='messagecommunication',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Professor'),
        ),
        migrations.AddField(
            model_name='messagecommunication',
            name='tid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.TA'),
        ),
        migrations.AddField(
            model_name='courseoffering',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Professor'),
        ),
        migrations.AddField(
            model_name='courseoffering',
            name='tid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.TA'),
        ),
        migrations.AddField(
            model_name='assignmentcommunication',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.Professor'),
        ),
        migrations.AddField(
            model_name='assignmentcommunication',
            name='tid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taco.TA'),
        ),
    ]
