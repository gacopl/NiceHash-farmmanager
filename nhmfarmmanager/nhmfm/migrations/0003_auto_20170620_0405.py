# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhmfm', '0002_auto_20170620_0223'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NHMHosts',
            new_name='NHMHost',
        ),
    ]