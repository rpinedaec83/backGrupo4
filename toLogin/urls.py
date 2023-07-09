from django.urls import path
from toLogin import views

urlpatterns = [
    path('api/signup', views.registro, name='signup'),
    path('api/login', views.logeo, name='login'),
]
