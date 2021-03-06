# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-13 11:22
from __future__ import unicode_literals

from django.db import migrations


def set_null_to_blank(queryset, fields):
    for element in queryset:
        for field in fields:
            value = getattr(element, field)
            if value is None:
                setattr(element, field, '')
        element.save()


def run_data_migration(apps, schema_editor):
    Attribute = apps.get_model('domain', 'Attribute')

    set_null_to_blank(Attribute.objects.all(), [
        'uri',
        'uri_prefix',
        'key',
        'path',
        'comment',
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0040_meta'),
    ]

    operations = [
        migrations.RunPython(run_data_migration),
    ]
