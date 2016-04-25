# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, null=True, max_length=50, verbose_name='Фамилия')),
                ('fam', models.CharField(blank=True, null=True, max_length=50, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, null=True, max_length=50, verbose_name='Пол')),
                ('text', models.TextField(verbose_name='Описание')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('city', models.CharField(blank=True, null=True, max_length=40, verbose_name='Город')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='app.Post'),
        ),
    ]
