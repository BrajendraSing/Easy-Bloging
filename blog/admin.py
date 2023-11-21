from django.contrib import admin
from django_summernote.widgets import SummernoteWidget
from blog.models.category import Category
from blog.models.post import Post
from django.db import models
# Register your models here.

class AdminPost(admin.ModelAdmin):
     formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget()},
    }

admin.site.register(Category)
admin.site.register(Post,AdminPost)
