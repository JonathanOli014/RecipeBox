from django.urls import path
from . import views  
from .views import (RecipeListView, RecipeDetailView,
                RecipeCreateView, RecipeUpdateView, RecipeDeleteView, list_recipes, update_profile_picture)

urlpatterns = [
    path('', RecipeListView.as_view(), name='list_recipe'),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='view_recipe'),
    path('home/add_recipe', RecipeCreateView.as_view(), name='add_recipe'),
    path('home/<int:pk>/edit', RecipeUpdateView.as_view(), name='update_recipe'),
    path('home/<int:pk>/delete', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('saved_recipe/', views.saved_recipes, name='saved_recipes'),
    path('recipe/<int:pk>/save/', views.save_recipe, name='save_recipe'),
     path('recipe/<int:pk>/', views.view_recipe, name='view_recipe'),
     path('allrecipes/', list_recipes, name='list_recipe'),
     path('update_profile_picture/', update_profile_picture, name='update_profile_picture'),
    #  path('profile/<int:user_id>/', views.view_profile, name='view_profilee'),
]