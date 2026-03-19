from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.lista_posts, name="index"),
    path('<slug:slug>', views.post_page, name="page")
]