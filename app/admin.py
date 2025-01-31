from django.contrib import admin
from .models import Category, Recipe, Ingredient, Instruction, SaveRecipes, Comment, Rating, UserProfile


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(SaveRecipes)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(UserProfile)


