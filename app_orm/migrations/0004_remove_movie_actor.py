# Generated by Django 3.2.25 on 2024-05-15 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0003_movie_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
    ]