# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160426_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='lng',
        ),
    ]
