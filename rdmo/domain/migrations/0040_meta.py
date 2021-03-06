# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0039_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this attribute (auto-generated).', max_length=640, null=True, verbose_name='URI'),
        ),
    ]
