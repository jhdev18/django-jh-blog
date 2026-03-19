from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.

def lista_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/lista_posts.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/page_post.html', {'post': post})