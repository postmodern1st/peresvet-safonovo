# Generated by Django 4.2.1 on 2023-05-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_slider_photo_trainer_delete_trainers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото галереи', 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Блог'},
        ),
        migrations.AlterModelOptions(
            name='slider_photo',
            options={'verbose_name': 'Фото слайдера', 'verbose_name_plural': 'Слайдер'},
        ),
    ]