# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-18 11:25
from __future__ import unicode_literals

import rdmo.core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domain', '0008_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.DurationField()),
                ('title_en', models.CharField(max_length=256)),
                ('title_de', models.CharField(max_length=256)),
                ('text_en', models.CharField(max_length=256)),
                ('text_de', models.CharField(max_length=256)),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='domain.Attribute')),
            ],
            options={
                'ordering': ('attribute',),
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
            bases=(rdmo.core.models.TranslationMixin, models.Model),
        ),
    ]