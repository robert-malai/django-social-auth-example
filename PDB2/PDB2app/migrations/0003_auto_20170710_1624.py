# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-10 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDB2app', '0002_auto_20170710_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectscopy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
