# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160426_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='lat',
            field=models.IntegerField(verbose_name='Lat', null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='lng',
            field=models.IntegerField(verbose_name='Lng', null=True),
        ),
    ]
