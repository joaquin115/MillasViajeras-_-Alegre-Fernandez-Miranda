from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import *

# Create your models here.

class Publicaciones(models.Model):
    imagen = models.ImageField(null=True, blank=True)
    pais = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)    
    descripcion = RichTextField(blank=True, null=True)
    fecha_viaje = models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 
    likes = models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name_plural = "Publicaciones"
        

class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)


class Comentario(models.Model):
    comentario = models.CharField(max_length=130)
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()