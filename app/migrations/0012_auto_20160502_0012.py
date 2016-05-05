# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_post_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_user',
            name='image',
            field=models.ImageField(default=False, upload_to='photos/%Y/%m/%d', blank=True),
        ),
    ]
