# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiscales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionvoluntario',
            name='mesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voluntarios', to='elecciones.Mesa'),
        ),
        migrations.AlterField(
            model_name='asignacionvoluntario',
            name='voluntario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='fiscales.Voluntario'),
        ),
    ]
