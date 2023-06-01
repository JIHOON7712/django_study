from django.shortcuts import render, redirect
from .models import Post,Comment

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {"posts" : posts}
    return render(request,'home.html',context = context)

def detail(request,pk):
    if request.method == 'POST':    
        content = request.POST.get('content')
        post = Post.objects.get(pk=pk)
        comment = Comment.objects.create(content=content,post=post)
        comment.save()
        return redirect('detail',pk=post.pk)
    else:
        post = Post.objects.get(pk=pk)
        comment = Comment.objects.filter(post=post)
        context = {"post" : post, "comment" : comment}
        return render(request,'post.html',context=context)



def create_post(request):
    # POST 요청이 들어오면
    if request.method == 'POST':    
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        post.save()
        return redirect('detail' , pk=post.pk)
    # GET 요청이 들어오면
    else:
        return render(request,'create_post.html')

