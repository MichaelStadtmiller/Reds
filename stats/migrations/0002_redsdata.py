# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
            ],
        ),
    ]
