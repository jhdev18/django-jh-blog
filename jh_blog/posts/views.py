from django.shortcuts import render

# Create your views here.

def lista_posts(request):
    return render(request, 'posts/lista_posts.html')