from django.contrib import admin
from .models import User, Recipe, Note

# Register your models here.
admin.site.register([User, Recipe, Note])