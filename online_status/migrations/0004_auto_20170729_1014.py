# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_status', '0003_auto_20170729_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinestatus',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
