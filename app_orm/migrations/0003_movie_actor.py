# Generated by Django 3.2.25 on 2024-05-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0002_auto_20240515_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.CharField(default='Saed', max_length=45),
            preserve_default=False,
        ),
    ]
