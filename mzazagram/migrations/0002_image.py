# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-21 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mzazagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_caption', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
