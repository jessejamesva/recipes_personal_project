# Generated by Django 3.2.12 on 2023-07-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_auto_20230717_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img_url',
            field=models.CharField(default='Missing Info', max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='User 1', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.CharField(default='Missing Info', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video_url',
            field=models.CharField(default='Missing Info', max_length=200),
        ),
    ]
