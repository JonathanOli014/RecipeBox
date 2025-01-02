from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Instruction, Category
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'
    
class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'app/list_recipe.html'

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'view_recipe'
    template_name = 'app/view_recipe.html'
    
class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'app/add_recipe.html'
    fields = ['recipeName', 'recipeCategory', 'createdBy']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['categories'] = Category.objects.all()
        # context['ingredients'] = Ingredient.objects.all()
        # context['instructions'] = Instruction.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        ingredients = self.request.POST.getlist('ingredients')
        instructions = self.request.POST.getlist('instruction')

        for name in ingredients:
            Ingredient.objects.create(recipe=self.object, name=name)

        for text in instructions:
            Instruction.objects.create(recipe=self.object, instruction=text)

        return response
    
class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'app/update_recipe.html'
    fields = ['recipeName', 'recipeCategory', 'createdBy']
    context_object_name = 'update_recipe'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.all()
            context['users'] = User.objects.all()
            context['selected_categories'] = self.object.recipeCategory.all().values_list('pk', flat=True)
            return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        ingredients = self.request.POST.getlist('ingredients')
        instructions = self.request.POST.getlist('instruction')

        self.object.ingredients.all().delete()
        self.object.instructions.all().delete()

        for name in ingredients:
            Ingredient.objects.create(recipe=self.object, name=name)

        for text in instructions:
            Instruction.objects.create(recipe=self.object, instruction=text)

        return response
    
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'app/delete_recipe.html'
    success_url = reverse_lazy('list_recipe')
