# Generated by Django 3.2.12 on 2023-07-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_alter_user_friends'),
        ('recipe_app', '0004_auto_20230718_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='saved_recipes',
            field=models.ManyToManyField(to='user_app.User'),
        ),
    ]