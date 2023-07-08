from django.contrib import admin
from .models import Cupon,Estado_pedido,Pedido, Detalle_pedido

# Register your models here.
admin.site.register(Cupon)
admin.site.register(Estado_pedido)
admin.site.register(Pedido)
admin.site.register(Detalle_pedido)
