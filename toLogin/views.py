from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.middleware.csrf import get_token

@api_view(['POST'])
def registro(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        # serializer.save()
        user = serializer.save()
        # login(request, user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def registro(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({'error': 'Se requieren username y password'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         user = User.objects.create_user(username=username, password=password)
#         # Realizar otras operaciones si es necesario
#         return Response({'success': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def logeo(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request._request, user)
        # Obtener el token CSRF
        csrf_token = get_token(request._request)
        # Devolver el token CSRF en la respuesta
        return Response({'message': 'Login successful', 'csrf_token': csrf_token}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
