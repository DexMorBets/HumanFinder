# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160430_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_user',
            name='image',
            field=models.ImageField(default=False, blank=True, upload_to='1'),
        ),
    ]
