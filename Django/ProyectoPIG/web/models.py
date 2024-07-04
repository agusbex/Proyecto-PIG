from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    numero_orden = models.CharField(max_length=10, unique=True)
    dni = models.CharField(max_length=8)
    estado = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.numero_orden

