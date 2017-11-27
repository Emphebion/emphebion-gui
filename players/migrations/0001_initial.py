# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(verbose_name='Player ID')),
                ('rfid', models.IntegerField(verbose_name='RFID tag')),
            ],
        ),
    ]
