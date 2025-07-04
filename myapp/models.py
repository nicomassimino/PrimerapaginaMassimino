from django.db import models

class Propiedad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='propiedades/', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metros_cuadrados = models.PositiveIntegerField(default=0)
    ambientes = models.PositiveIntegerField(default=1)
    patio = models.BooleanField(default=False)
    balcon = models.BooleanField(default=False)
    zona = models.CharField(max_length=50, default="Sin zona")  # NUEVO

    def __str__(self):
        return self.titulo

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField()
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
