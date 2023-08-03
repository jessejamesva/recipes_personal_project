from django.urls import path
from .views import Recipes_info, Recipe_info


urlpatterns = [
    path('', Recipes_info.as_view(), name='all_recipes'),
    path('<int:pk>/', Recipe_info.as_view(), name ='a_recipe')
]