# Generated by Django 4.1.3 on 2022-12-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20, verbose_name='Имя')),
                ('email', models.EmailField(max_length=30, verbose_name='Почта')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
        ),
    ]