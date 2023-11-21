from django.shortcuts import render
from django.views.generic import View
from blog.models.post import Post
from blog.models.category import Category

class Home(View):
    def get(self,request):
        context = {}
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()
        context['recent_posts'] = Post.objects.all().order_by('-id')
        
        if request.GET.get('search'):
            search = request.GET.get('search')
            context['posts'] = Post.objects.filter(title__contains=search)
        
        return render(request,'home.html',context)
    

    
    
    
