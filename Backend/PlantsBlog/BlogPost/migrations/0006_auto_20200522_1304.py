# Generated by Django 3.0.6 on 2020-05-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0005_auto_20200522_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantpost',
            name='image',
            field=models.ImageField(upload_to='post_titles', verbose_name='Титульне зображення'),
        ),
    ]