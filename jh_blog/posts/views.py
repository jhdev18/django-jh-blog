from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def lista_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/lista_posts.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/page_post.html', {'post': post})

@login_required(login_url='/users/login/')
def novo_post(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            novo_post = form.save(commit=False)
            novo_post.autor = request.user
            novo_post.save()
            return redirect('posts:index')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/novo_post.html', {'form' : form})
