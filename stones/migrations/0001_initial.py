# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0003_player_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_type', models.CharField(choices=[('0', 'Denied'), ('1', 'Granted'), ('2', 'Forcible')], max_length=1, verbose_name='Access type')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('stone_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Stone ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Stone name')),
            ],
        ),
        migrations.AddField(
            model_name='access',
            name='stone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stones.Stone'),
        ),
    ]
