from django.db import models
from user_app.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50, unique=True, default='User 1')
    rating = models.DecimalField(max_digits=6, decimal_places=5, default=0.99999)
    description = models.TextField(default='Missing Info')
    ingredients = models.TextField(default='Missing Info')
    instructions = models.TextField(default='Missing Info')
    img_url = models.CharField(max_length=200, default='Missing Info')
    video_url = models.CharField(max_length=200, default='Missing Info')
    servings = models.PositiveIntegerField(default=2)
    slug = models.CharField(max_length=50, default='Missing Info')

    saved_by = models.ManyToManyField(User, related_name="saved_recipes")

    def __str__(self):
        return self.name
