# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carride', '0033_vehicle_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
    ]
