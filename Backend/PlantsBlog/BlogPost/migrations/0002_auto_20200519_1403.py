# Generated by Django 3.0.6 on 2020-05-19 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show',
            field=models.BooleanField(default=False, verbose_name='Готово для показу'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static/images/post_titles', verbose_name='Титульне зображення'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogPost.Post')),
            ],
        ),
    ]