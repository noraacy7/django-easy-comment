# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0027_auto_20170721_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
    ]
