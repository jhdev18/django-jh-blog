from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=75)
    texto = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo