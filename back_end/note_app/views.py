from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from rest_framework.views import APIView, Response
from .models import Note
import json


class Notes_info(APIView):
    def get(self, request):
        all_notes = Note.objects.all()
        json_notes = json.loads(serialize('json', all_notes))
        # for current_user in range(len(json_users)):
        #     json_users[current_user]['fields']['friends'] = json.loads(serialize('json', all_users[current_user].friends.all()))
        return Response(json_notes)

class Note_info(APIView):
    def get(self, request, pk):
        a_note = get_object_or_404(Note, pk = pk)
        json_user = json.loads(serialize('json', [a_note]))[0]
        return Response(json_user)