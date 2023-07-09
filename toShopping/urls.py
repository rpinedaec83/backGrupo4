from django.urls import include, path
from rest_framework import routers
from .views import CuponViewSet, EstadoPedidoViewSet, PedidoViewSet, DetallePedidoViewSet

router = routers.DefaultRouter()
router.register(r'cupones', CuponViewSet)
router.register(r'estados-pedido', EstadoPedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
