# Generated by Django 4.1.3 on 2022-12-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('contacts', models.CharField(max_length=20, verbose_name='Контакты')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]