# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color_name', models.CharField(max_length=100, blank=True, verbose_name='Цвет', null=True)),
                ('color_code', models.CharField(max_length=100, blank=True, verbose_name='Код цвета', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital_name', models.CharField(max_length=100, verbose_name='Название больницы')),
                ('hospital_adress', models.CharField(max_length=100, verbose_name='Адрес')),
                ('hospital_number1', models.CharField(max_length=25, verbose_name='Номер1')),
                ('hospital_number2', models.CharField(max_length=25, verbose_name='Номер2')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.IntegerField(blank=True, verbose_name='Возраст', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=40, blank=True, verbose_name='Телосложение', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='boots',
            field=models.CharField(max_length=40, blank=True, verbose_name='Обувь', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='eyes_color',
            field=models.CharField(max_length=40, blank=True, verbose_name='Цвет глаз', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hair_color',
            field=models.CharField(max_length=40, blank=True, verbose_name='Цвет волос', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hat',
            field=models.CharField(max_length=40, blank=True, verbose_name='Головной убор', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='height',
            field=models.IntegerField(blank=True, verbose_name='Рост', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='konech',
            field=models.BooleanField(verbose_name='Отсутсвие конечностей', default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='niz',
            field=models.CharField(max_length=40, blank=True, verbose_name='Штаны', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='protez',
            field=models.BooleanField(verbose_name='Протезы', default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='shramy',
            field=models.BooleanField(verbose_name='Шрамы', default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='tatu',
            field=models.BooleanField(verbose_name='Тату', default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='vverh',
            field=models.CharField(max_length=40, blank=True, verbose_name='Верхняя одежда', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='gender',
            field=models.CharField(max_length=40, blank=True, verbose_name='Пол', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата публикации', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, verbose_name='Описание', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='boots_color',
            field=models.ForeignKey(to='app.Color', verbose_name='Цвет обуви', null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='post',
            name='hat_color',
            field=models.ForeignKey(to='app.Color', verbose_name='Цвет головного убора', null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='post',
            name='hospital',
            field=models.ForeignKey(to='app.Hospital', verbose_name='Больница', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='niz_color',
            field=models.ForeignKey(to='app.Color', verbose_name='Цвет нижней одежды', null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='post',
            name='vverh_color',
            field=models.ForeignKey(to='app.Color', verbose_name='Цвет верхней одежды', null=True, related_name='+'),
        ),
    ]
