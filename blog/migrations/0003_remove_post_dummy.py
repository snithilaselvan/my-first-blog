# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_dummy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dummy',
        ),
    ]
