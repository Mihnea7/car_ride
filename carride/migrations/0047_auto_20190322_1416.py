# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-22 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carride', '0046_auto_20190322_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='static\\images\\default.jpeg', upload_to='profile_images'),
        ),
    ]
