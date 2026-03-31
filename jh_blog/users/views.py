from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:index")
    else:
        form = UserCreationForm()
    return render(request, "users/registro_page.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:index")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def sair_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:index")