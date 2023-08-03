from django.urls import path
from .views import Users_info, User_info


urlpatterns = [
    path('', Users_info.as_view(), name='all_Users'),
    path('<int:pk>/', User_info.as_view(), name ='a_User')
]