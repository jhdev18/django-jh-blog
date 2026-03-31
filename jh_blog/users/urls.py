from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('registro/', views.registro , name="registro"),
    path('login/', views.login_view, name="login"),
    path('sair/', views.sair_view, name="sair"),
]