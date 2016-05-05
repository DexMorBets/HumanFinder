# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160418_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='boots_color',
            field=models.ForeignKey(null=True, verbose_name='Цвет обуви', related_name='+', to='app.Color', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='hat_color',
            field=models.ForeignKey(null=True, verbose_name='Цвет головного убора', related_name='+', to='app.Color', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='niz_color',
            field=models.ForeignKey(null=True, verbose_name='Цвет нижней одежды', related_name='+', to='app.Color', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='vverh_color',
            field=models.ForeignKey(null=True, verbose_name='Цвет верхней одежды', related_name='+', to='app.Color', blank=True),
        ),
    ]
