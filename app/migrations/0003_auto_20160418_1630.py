# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160418_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_adress',
            field=models.CharField(null=True, max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(null=True, max_length=100, verbose_name='Название больницы'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_number1',
            field=models.CharField(null=True, max_length=25, verbose_name='Номер1'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_number2',
            field=models.CharField(null=True, max_length=25, verbose_name='Номер2'),
        ),
    ]
