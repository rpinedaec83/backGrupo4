from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, Group, Permission, PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
    # Agrega campos adicionales si los necesitas
    
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    # modificar el campo 'user_permissions' con el argumento 'related_name'
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
    
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Agrega campos adicionales para el perfil de usuario si los necesitas
