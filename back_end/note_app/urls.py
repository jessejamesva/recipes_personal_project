from django.urls import path
from .views import Notes_info, Note_info


urlpatterns = [
    path('', Notes_info.as_view(), name='all_Notes'),
    path('<int:pk>/', Note_info.as_view(), name ='a_Note')
]