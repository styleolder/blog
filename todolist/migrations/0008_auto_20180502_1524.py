# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-02 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(default=None, max_length=11, verbose_name='\u624b\u673a\u53f7\u7801'),
        ),
    ]
