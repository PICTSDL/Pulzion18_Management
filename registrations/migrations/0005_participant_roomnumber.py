# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-04 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_auto_20180604_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='roomNumber',
            field=models.CharField(default=None, max_length=4),
            preserve_default=False,
        ),
    ]
