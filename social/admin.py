from django.contrib import admin
from .models import Profile, Recipe, Comment, Group

admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Group)