# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160502_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_user',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos', default=False),
        ),
    ]
