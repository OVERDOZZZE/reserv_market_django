from django.db import models

# Create your models here.


class Offer(models.Model):
    name = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')
    contacts = models.CharField('Контакты', max_length=20)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
