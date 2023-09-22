from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


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
    technincs = models.CharField(max_length = 500)
    tecNumber = models.CharField(max_length = 100)
    time = models.CharField(max_length = 50, default = "00.00.0000")
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
        
class File(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()
    
    class Meta:
        verbose_name = 'Загрузка xml'
        verbose_name_plural = 'Загрузка xml'

    