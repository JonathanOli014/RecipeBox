from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Recipe(models.Model):
    recipeName = models.CharField(max_length=200)
    recipeCategory = models.ManyToManyField(Category, related_name= 'RecipeCategory')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipeName
    
    def get_absolute_url(self):
        return reverse("view_recipe", kwargs={"pk": self.pk})

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.recipe.recipeName

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='instructions', on_delete=models.CASCADE)
    instruction = models.TextField()

    def __str__(self):
        return self.recipe.recipeName
        
class RecipeCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collectionName = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.collectionName

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.recipe}'
    
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def __str__(self):
        return f'Rating {self.score} by {self.user} for {self.recipe}'

