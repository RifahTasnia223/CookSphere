from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
    path('comment/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]