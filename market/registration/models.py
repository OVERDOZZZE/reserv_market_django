from django.db import models

# Create your models here.


class Registration(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта', max_length=30)
    password = models.CharField('Пароль', max_length=30)

