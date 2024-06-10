from django.db import models

# Create your models here.
class formulario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email") 
    mensaje = models.TextField(verbose_name="mensaje")
    