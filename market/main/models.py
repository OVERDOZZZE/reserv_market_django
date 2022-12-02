from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='images/', default='default/ak47.jpg')

    def __str__(self):
        return self.title
