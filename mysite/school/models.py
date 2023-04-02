from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# class Castomer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     login = models.CharField(max_length=30, verbose_name= 'Логин')
#     password = models.CharField(max_length=30, verbose_name='Пароль')
    
#     def __str__(self):
#         return self.password

#     class Meta:
#         verbose_name = 'Авторизация'
#         verbose_name_plural = 'Авторизация'

# class Adress(models.Model):
#     adress = models.CharField(max_length = 50, verbose_name = 'Адресс')

#     def __str__(self):
#         return self.adress

#     class Meta:
#         verbose_name = 'Здание'
#         verbose_name_plural = 'Здания'

class Accounting(models.Model):
    users = models.CharField(max_length = 30, verbose_name = 'Пользователь')
    technincs = models.CharField(max_length = 50, verbose_name = 'Техника')
    create = models.DateField(auto_now = True)
    tecNumber = models.IntegerField(verbose_name = 'Техномер')

    def __str__(self):
        return self.users

    class Meta:
        verbose_name = 'Учётная книга'
        verbose_name_plural = 'Учётная книга'
    

class Store(models.Model):
    technincs = models.CharField(max_length = 50)
    tecNumber = models.IntegerField()
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

# class User(models.Model):
#     jobtitle = models.CharField(max_length = 30, verbose_name = 'Должность')

#     def __str__(self):
#         return self.jobtitle

#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
    