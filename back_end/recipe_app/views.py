from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from rest_framework.views import APIView, Response
from .models import Recipe
from user_app.models import User
from note_app.models import Note
import json


def set_up_recipe_info(a_recipe, recipe_query):
    recipe_notes = list(Note.objects.filter(recipe_id=a_recipe['pk']).values())
    a_recipe['fields']['recipe_notes'] = recipe_notes
    a_recipe['fields']['saved_by'] = json.loads(serialize('json', recipe_query.saved_by.all()))


# Create your views here.
class Recipes_info(APIView):
    def get(self, request):
        all_recipes = Recipe.objects.all()
        json_recipes = json.loads(serialize('json', all_recipes))
        for current_recipe in range(len(json_recipes)):
            set_up_recipe_info(json_recipes[current_recipe], all_recipes[current_recipe])
        return Response(json_recipes)

class Recipe_info(APIView):
    def get(self, request, pk):
        a_recipe = get_object_or_404(Recipe, pk = pk)
        json_recipe = json.loads(serialize('json', [a_recipe]))[0]
        set_up_recipe_info(json_recipe, a_recipe)
        return Response(json_recipe)

