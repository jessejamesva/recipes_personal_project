from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from rest_framework.views import APIView, Response
from .models import User
from recipe_app.models import Recipe
from note_app.models import Note
import json


def set_up_user_info(user, all_users):
    user_saved_recipes = list(Recipe.objects.filter(saved_by = user['pk']).values())
    user_created_notes = list(Note.objects.filter(user = user['pk']).values())
    user['fields']['saved_recipes'] = user_saved_recipes
    user['fields']['user_notes'] = user_created_notes
    user['fields']['friends'] = json.loads(serialize('json', all_users.friends.all()))

class Users_info(APIView):
    def get(self, request):
        all_users = User.objects.all()
        json_users = json.loads(serialize('json', all_users))
        for current_user in range(len(json_users)):
            set_up_user_info(json_users[current_user], all_users[current_user])
        return Response(json_users)

class User_info(APIView):
    def get(self, request, pk):
        a_user = get_object_or_404(User, pk = pk)
        json_user = json.loads(serialize('json', [a_user]))[0]
        set_up_user_info(json_user, a_user)
        return Response(json_user)