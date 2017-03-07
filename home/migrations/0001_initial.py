# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=2)),
                ('price', models.IntegerField()),
            ],
        ),
    ]