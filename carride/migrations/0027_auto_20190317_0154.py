# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-17 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carride', '0026_auto_20190316_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]