# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 08:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=128, unique=True)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]