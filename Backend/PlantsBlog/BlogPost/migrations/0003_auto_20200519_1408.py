# Generated by Django 3.0.6 on 2020-05-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0002_auto_20200519_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='Улюблене'),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]