# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-21 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0121_auto_20161220_0106'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerWithdrawl',
            new_name='PlayerWithdrawal',
        ),
    ]