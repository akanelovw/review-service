from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title
from users.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Review)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Comment)
