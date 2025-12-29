from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from .models import ColorChange
from .serializers import UserSerializer, ColorChangeSerializer, RegisterSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class ColorChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        last_change = ColorChange.get_last_change()
        return Response(last_change)
    
    def post(self, request):
        color = ColorChange.generate_random_color()
        color_change = ColorChange.objects.create(
            user=request.user,
            color=color
        )

        last_change = ColorChange.get_last_change()
        return Response({
            'color': color,
            'last_change': last_change
        })
    
class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)