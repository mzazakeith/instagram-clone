# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 17:25
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('mzazagram', '0006_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=pyuploadcare.dj.models.ImageField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
