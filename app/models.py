from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

    def __str__(self):
        return self.user.username
    
class Recipe(models.Model):
    recipeName = models.CharField(max_length=200)
    recipeCategory = models.ManyToManyField(Category, related_name= 'RecipeCategory')
    recipeDescription = models.TextField(default='No description provided')
    recipeImage = models.ImageField(upload_to='images/', default='images/default.jpg')
    servings = models.IntegerField(default=1)
    cookTime = models.IntegerField(default=0)
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
        
class SaveRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe, related_name='saved_recipes')

def __str__(self):
        return f'Saved Recipes by {self.user.username}'

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
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.recipe.recipeName} - {self.score} by {self.user.username}'

