from django.db import models
from ckeditor.fields import RichTextField

class Propiedad(models.Model):
    titulo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='propiedades/')
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.ubicacion}"
