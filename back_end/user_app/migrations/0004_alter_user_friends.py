# Generated by Django 3.2.12 on 2023-07-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20230718_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_user_app_user_friends_+', to='user_app.User'),
        ),
    ]