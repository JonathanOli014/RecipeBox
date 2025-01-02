from django.urls import path
from .views import (HomePageView, AboutPageView, RecipeListView, RecipeDetailView,
                RecipeCreateView, RecipeUpdateView, RecipeDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list_recipe', RecipeListView.as_view(), name='list_recipe'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('home/<int:pk>', RecipeDetailView.as_view(), name='view_recipe'),
    path('home/add_recipe', RecipeCreateView.as_view(), name='add_recipe'),
    path('home/<int:pk>/edit', RecipeUpdateView.as_view(), name='update_recipe'),
    path('home/<int:pk>/delete', RecipeDeleteView.as_view(), name='delete_recipe'),
]