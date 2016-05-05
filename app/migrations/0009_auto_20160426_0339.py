# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160426_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='lat',
            field=models.CharField(verbose_name='Lat', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='lng',
            field=models.CharField(verbose_name='Lng', max_length=25, null=True),
        ),
    ]
