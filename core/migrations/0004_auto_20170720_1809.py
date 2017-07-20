# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='data_de_nascimento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='ranking',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
