# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-02 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.IntegerField(unique=True)),
                ('model', models.CharField(max_length=256, unique=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=10, max_length=10)),
                ('year', models.IntegerField()),
                ('new', models.BooleanField(default=True)),
                ('username', models.CharField(blank=True, max_length=20)),
                ('phoneNum', models.CharField(blank=True, max_length=13)),
                ('additionalInfo', models.CharField(max_length=1024)),
            ],
        ),
    ]
