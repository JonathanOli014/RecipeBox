
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Instruction, Category, SaveRecipes, Comment, Rating
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render
from .forms import ProfilePictureForm

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    fields = '__all__'
    template_name = 'app/list_recipe.html'

    def get_queryset(self):
        return Recipe.objects.all().order_by('-createdAt')

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'view_recipe'
    template_name = 'app/view_recipe.html'

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'app/add_recipe.html'
    fields = ['recipeName', 'recipeCategory', 'recipeImage', 'servings', 'cookTime']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
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
    fields = ['recipeName','recipeCategory','recipeDescription','recipeImage','servings', 'cookTime']
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

        if 'recipeImage' in self.request.FILES:
            form.instance.recipeImage = self.request.FILES['recipeImage']

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

def view_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    recipes = Recipe.objects.filter(createdBy=user)
    return render(request, 'app/view_profile.html', {
        'profile_user': user,
        'recipes': recipes,
    })

@login_required
def save_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    saved_recipes, created = SaveRecipes.objects.get_or_create(user=request.user)
    saved_recipes.recipes.add(recipe)
    return redirect('saved_recipes')

@login_required
def saved_recipes(request):
    saved_recipes = SaveRecipes.objects.filter(user=request.user).first()
    recipes = saved_recipes.recipes.all() if saved_recipes else []
    return render(request, 'app/saved_recipes.html', {
        'recipes': recipes,
    })

def view_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    creator = recipe.createdBy
    recipe_count = Recipe.objects.filter(createdBy=creator).count()
    comments = Comment.objects.filter(recipe=recipe).order_by('-createdAt')
    ratings = Rating.objects.filter(recipe=recipe)
    average_rating = ratings.aggregate(Avg('score'))['score__avg'] if ratings.exists() else None
    can_rate = request.user != creator

    if request.method == 'POST':
        if 'comment' in request.POST:
            text = request.POST.get('text')
            if text:
                Comment.objects.create(recipe=recipe, user=request.user, text=text)
        elif 'rating' in request.POST:
            score = request.POST.get('score')
            if score:
                Rating.objects.update_or_create(recipe=recipe, user=request.user, defaults={'score': score})

        return redirect('view_recipe', pk=recipe.pk)

    return render(request, 'app/view_recipe.html', {
        'view_recipe': recipe,
        'recipe_count': recipe_count,
        'comments': comments,
        'average_rating': average_rating,
        'can_rate': can_rate,
    })

def list_recipes(request):
    query = request.GET.get('search')
    if query:
        recipes = Recipe.objects.filter(recipeName__icontains=query)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'app/list_recipe.html', {'recipes': recipes})

@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('view_profile', user_id=request.user.pk)
    else:
        form = ProfilePictureForm(instance=request.user.userprofile)
    return render(request, 'app/view_profile.html', {'form': form})