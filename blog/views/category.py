from django.shortcuts import render
from django.views import View
from blog.models.post import Post
from blog.models.category import Category

class CategoryView(View):
    def get(self,request,category_id):
        context = {}
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.all().order_by('-id')
        context['posts'] = Post.objects.filter(category=category_id).order_by('-id')

        return render(request,'category.html',context)