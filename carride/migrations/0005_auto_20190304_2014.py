# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-04 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carride', '0004_auto_20190304_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='picture',
            field=models.ImageField(blank=True, upload_to='car_images'),
        ),
    ]
