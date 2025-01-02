from django.contrib import admin
from .models import Category, Recipe, Ingredient, Instruction, RecipeCollection, Comment, Rating

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(RecipeCollection)
admin.site.register(Comment)
admin.site.register(Rating)

