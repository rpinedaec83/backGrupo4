from django.urls import include, path
from rest_framework import routers
from .views import CategoriaViewSet, ProductoViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
