from django.contrib import admin
from .models import Comment, Post, Category, PostView
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)