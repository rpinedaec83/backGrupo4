from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extraemos la contraseña del diccionario de datos validados
        user = CustomUser.objects.create_user(**validated_data, password=password)  # Pasamos la contraseña como argumento
        return user
