from rest_framework import viewsets
from .models import Cupon, Estado_pedido, Pedido, Detalle_pedido
from .serializers import CuponSerializer, EstadoPedidoSerializer, PedidoSerializer, DetallePedidoSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@method_decorator(csrf_protect, name='dispatch')
class CuponViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

@method_decorator(csrf_protect, name='dispatch')
class EstadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = Estado_pedido.objects.all()
    serializer_class = EstadoPedidoSerializer

@method_decorator(csrf_protect, name='dispatch')
class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = Detalle_pedido.objects.all()
    serializer_class = DetallePedidoSerializer

@method_decorator(csrf_protect, name='dispatch')
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
