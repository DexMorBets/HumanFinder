# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User)
    name = models.CharField(blank=True, verbose_name="Имя", max_length=50, null=True)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, null=True, blank=True)
    fam = models.CharField(verbose_name="Отчество", max_length=50, null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=40, null=True, blank=True)
    text = models.TextField(verbose_name='Описание', null=True, blank=True)
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)
    height = models.IntegerField(verbose_name='Рост', null=True, blank=True)
    body = models.CharField(verbose_name='Телосложение', max_length=40, null=True, blank=True)
    eyes_color = models.CharField(verbose_name='Цвет глаз', max_length=40, null=True, blank=True)
    hair_color = models.CharField(verbose_name='Цвет волос', max_length=40, null=True, blank=True)
    shramy = models.BooleanField(verbose_name='Шрамы', default=False, blank=True)
    tatu = models.BooleanField(verbose_name='Тату', default=False, blank=True)
    protez = models.BooleanField(verbose_name='Протезы', default=False, blank=True)
    konech = models.BooleanField(verbose_name='Отсутсвие конечностей', default=False, blank=True)

    hat = models.CharField(verbose_name='Головной убор', max_length=40, null=True, blank=True)
    hat_color = models.ForeignKey('Color', verbose_name='Цвет головного убора', null=True, related_name='+', blank=True)
    vverh = models.CharField(verbose_name='Верхняя одежда', max_length=40, null=True, blank=True)
    vverh_color = models.ForeignKey('Color', verbose_name='Цвет верхней одежды', null=True, related_name='+', blank=True)
    niz = models.CharField(verbose_name='Штаны', max_length=40, null=True, blank=True)
    niz_color = models.ForeignKey('Color', verbose_name='Цвет нижней одежды', null=True, related_name='+', blank=True)
    boots = models.CharField(verbose_name='Обувь', max_length=40, null=True, blank=True)
    boots_color = models.ForeignKey('Color', verbose_name='Цвет обуви', null=True, related_name='+', blank=True)

    hospital = models.ForeignKey('Hospital', verbose_name='Больница', null=True)


    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата публикации')
    city = models.CharField(verbose_name='Город', max_length=40, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.fam

class Post_user(models.Model):
    author = models.ForeignKey(User)
    name = models.CharField(blank=True, verbose_name="Имя", max_length=50, null=True)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, null=True, blank=True)
    fam = models.CharField(verbose_name="Отчество", max_length=50, null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=40, null=True, blank=True)
    text = models.TextField(verbose_name='Описание', null=True, blank=True)
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)
    height = models.IntegerField(verbose_name='Рост', null=True, blank=True)
    body = models.CharField(verbose_name='Телосложение', max_length=40, null=True, blank=True)
    eyes_color = models.CharField(verbose_name='Цвет глаз', max_length=40, null=True, blank=True)
    hair_color = models.CharField(verbose_name='Цвет волос', max_length=40, null=True, blank=True)
    shramy = models.BooleanField(verbose_name='Шрамы', default=False, blank=True)
    tatu = models.BooleanField(verbose_name='Тату', default=False, blank=True)
    protez = models.BooleanField(verbose_name='Протезы', default=False, blank=True)
    konech = models.BooleanField(verbose_name='Отсутсвие конечностей', default=False, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', default=False, blank=True)

    hat = models.CharField(verbose_name='Головной убор', max_length=40, null=True, blank=True)
    hat_color = models.ForeignKey('Color', verbose_name='Цвет головного убора', null=True, related_name='+', blank=True)
    vverh = models.CharField(verbose_name='Верхняя одежда', max_length=40, null=True, blank=True)
    vverh_color = models.ForeignKey('Color', verbose_name='Цвет верхней одежды', null=True, related_name='+', blank=True)
    niz = models.CharField(verbose_name='Штаны', max_length=40, null=True, blank=True)
    niz_color = models.ForeignKey('Color', verbose_name='Цвет нижней одежды', null=True, related_name='+', blank=True)
    boots = models.CharField(verbose_name='Обувь', max_length=40, null=True, blank=True)
    boots_color = models.ForeignKey('Color', verbose_name='Цвет обуви', null=True, related_name='+', blank=True)

    address = models.CharField(verbose_name="Адресс", max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Телефон", max_length=50, null=True, blank=True)

    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата публикации')
    city = models.CharField(verbose_name='Город', max_length=40, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.fam

class Hospital(models.Model):
    hospital_name = models.CharField(verbose_name='Название больницы', max_length=100, null=True)
    hospital_adress = models.CharField(verbose_name='Адрес', max_length=100, null=True)
    hospital_number1 = models.CharField(verbose_name='Номер1', max_length=25, null=True)
    hospital_number2 = models.CharField(verbose_name='Номер2', max_length=25, null=True)
    lat = models.CharField(verbose_name='Lat', max_length=25, null=True)
    lng = models.CharField(verbose_name='Lng', max_length=25, null=True)

    def __str__(self):
        return self.hospital_name

class Color(models.Model):
    color_name = models.CharField(verbose_name='Цвет', max_length=100, null=True, blank=True)
    color_code = models.CharField(verbose_name='Код цвета', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.color_name

class Comment(models.Model):
    post = models.ForeignKey('app.Post', related_name='comments')
    author = models.CharField(verbose_name='Автор', max_length=200)
    text = models.TextField(verbose_name='Текст комментария',)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Comment_user(models.Model):
    post = models.ForeignKey('app.Post_user', related_name='comments')
    author = models.CharField(verbose_name='Автор', max_length=200)
    text = models.TextField(verbose_name='Текст комментария',)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text