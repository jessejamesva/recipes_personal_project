from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=25, unique=True, default='User 1')
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.user_name