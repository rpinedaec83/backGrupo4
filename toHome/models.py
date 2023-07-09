from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    igv = models.BooleanField(default=True)
    imagen = models.FileField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)
    imagen1 = models.FileField(blank=True,null=True)
    def __str__(self):
        return self.nombre