from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment, Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'required': True, 'class': 'form-control', 'placeholder': 'Title (required)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (optional)', 'rows': 2}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingredients (optional)', 'rows': 2}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instructions (optional)', 'rows': 2}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['description'].required = False
        self.fields['ingredients'].required = False
        self.fields['instructions'].required = False
        self.fields['image'].required = False

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_pic']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

# Home page: show all recipes, likes, comments, and allow like/comment if logged in

def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    # Prepare a list of (recipe, comment_form) tuples for template
    recipe_forms = [(recipe, CommentForm()) for recipe in recipes]
    liked_ids = []
    if request.user.is_authenticated:
        liked_ids = [r.id for r in recipes if request.user in r.likes.all()]
    # Fetch all profiles for authors in the feed
    author_profiles = {profile.user_id: profile for profile in Profile.objects.filter(user__in=[r.author for r in recipes])}
    return render(request, 'social/home.html', {
        'recipe_forms': recipe_forms,
        'liked_ids': liked_ids,
        'author_profiles': author_profiles,
    })

@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user not in recipe.likes.all():
        recipe.likes.add(request.user)
        messages.success(request, 'You liked this recipe!')
    else:
        recipe.likes.remove(request.user)
        messages.info(request, 'You unliked this recipe!')
    return redirect('social:home')

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Comment added!')
    return redirect('social:home')

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Recipe created!')
            return redirect('social:home')
    else:
        form = RecipeForm()
    return render(request, 'social/create_recipe.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'social/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('social:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'social/edit_profile.html', {'form': form})

# Add a view to show any user's profile by username
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'social/profile.html', {'profile': profile, 'viewed_user': user})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        messages.error(request, 'You are not allowed to delete this post.')
        return redirect('social:home')
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted!')
        return redirect('social:home')
    return render(request, 'social/confirm_delete.html', {'recipe': recipe})