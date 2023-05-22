from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {"posts" : posts
               }
    return render(request,'home.html',context = context)

def detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {"post" : post}
    return render(request,'post.html',context=context)