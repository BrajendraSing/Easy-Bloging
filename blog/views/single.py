from django.shortcuts import render
from django.views.generic import View
from blog.models.post import Post
from blog.models.category import Category


class Single(View):
    def get(self,request,post_id):
        context = {}
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.all().order_by('-id')
        context['post'] = Post.objects.get(id=post_id)
        
        return render(request,'single.html',context)