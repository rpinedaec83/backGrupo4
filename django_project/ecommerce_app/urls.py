from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/<slug:product_slug>/', views.show_product, name='product_detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
<<<<<<< HEAD
=======
    path('compras/', views.compra_list_create, name='compra-list-create'),
    path('compras/<int:pk>/', views.compra_detail, name='compra-detail'),
>>>>>>> aa7d97c01d047dfcbdfc657835622d4f05caec18
]
