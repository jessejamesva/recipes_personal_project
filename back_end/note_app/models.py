from django.db import models
from user_app.models import User
from recipe_app.models import Recipe

# Create your models here.
class Note(models.Model):
    note_text = models.TextField(default="This recipe was great as is!!")
    user = models.ForeignKey(User, related_name="created_notes", on_delete=models.CASCADE, default=1)
    recipe = models.ForeignKey(Recipe, related_name="user_notes", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.note_text[:21]