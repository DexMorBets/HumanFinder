# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160502_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_user',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default=False),
        ),
    ]
