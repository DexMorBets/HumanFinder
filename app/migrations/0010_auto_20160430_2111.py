# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_auto_20160426_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_user',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('author', models.CharField(verbose_name='Автор', max_length=200)),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post_user',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, blank=True, verbose_name='Имя', max_length=50)),
                ('surname', models.CharField(null=True, blank=True, verbose_name='Фамилия', max_length=50)),
                ('fam', models.CharField(null=True, blank=True, verbose_name='Отчество', max_length=50)),
                ('gender', models.CharField(null=True, blank=True, verbose_name='Пол', max_length=40)),
                ('text', models.TextField(null=True, blank=True, verbose_name='Описание')),
                ('age', models.IntegerField(null=True, blank=True, verbose_name='Возраст')),
                ('height', models.IntegerField(null=True, blank=True, verbose_name='Рост')),
                ('body', models.CharField(null=True, blank=True, verbose_name='Телосложение', max_length=40)),
                ('eyes_color', models.CharField(null=True, blank=True, verbose_name='Цвет глаз', max_length=40)),
                ('hair_color', models.CharField(null=True, blank=True, verbose_name='Цвет волос', max_length=40)),
                ('shramy', models.BooleanField(default=False, verbose_name='Шрамы')),
                ('tatu', models.BooleanField(default=False, verbose_name='Тату')),
                ('protez', models.BooleanField(default=False, verbose_name='Протезы')),
                ('konech', models.BooleanField(default=False, verbose_name='Отсутсвие конечностей')),
                ('hat', models.CharField(null=True, blank=True, verbose_name='Головной убор', max_length=40)),
                ('vverh', models.CharField(null=True, blank=True, verbose_name='Верхняя одежда', max_length=40)),
                ('niz', models.CharField(null=True, blank=True, verbose_name='Штаны', max_length=40)),
                ('boots', models.CharField(null=True, blank=True, verbose_name='Обувь', max_length=40)),
                ('address', models.CharField(null=True, blank=True, verbose_name='Адресс', max_length=100)),
                ('phone_number', models.CharField(null=True, blank=True, verbose_name='Телефон', max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')),
                ('city', models.CharField(null=True, blank=True, verbose_name='Город', max_length=40)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('boots_color', models.ForeignKey(null=True, to='app.Color', related_name='+', blank=True, verbose_name='Цвет обуви')),
                ('hat_color', models.ForeignKey(null=True, to='app.Color', related_name='+', blank=True, verbose_name='Цвет головного убора')),
                ('niz_color', models.ForeignKey(null=True, to='app.Color', related_name='+', blank=True, verbose_name='Цвет нижней одежды')),
                ('vverh_color', models.ForeignKey(null=True, to='app.Color', related_name='+', blank=True, verbose_name='Цвет верхней одежды')),
            ],
        ),
        migrations.AddField(
            model_name='comment_user',
            name='post',
            field=models.ForeignKey(to='app.Post_user', related_name='comments'),
        ),
    ]
