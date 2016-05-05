# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160426_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='lat',
            field=models.DecimalField(verbose_name='Lat', decimal_places=6, null=True, max_digits=15),
        ),
        migrations.AddField(
            model_name='hospital',
            name='lng',
            field=models.DecimalField(verbose_name='Lng', decimal_places=6, null=True, max_digits=15),
        ),
    ]
