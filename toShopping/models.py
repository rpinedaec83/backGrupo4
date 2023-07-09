from django.db import models
from toHome.models import Producto
from toLogin.models import CustomUser

# Create your models here.
class Cupon(models.Model):
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    descuento = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.codigo

class Estado_pedido(models.Model):
    descripcion = models.CharField(max_length=200, default="enCarrito")
    def __str__(self):
        return self.descripcion

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    igv = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado_pedido, on_delete=models.CASCADE)
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return f"Pedido N° {self.id}"

class Detalle_pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"Detalle del pedido {self.pedido.id} - Usuario: {self.pedido.user.username}"