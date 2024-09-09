from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer
from .serializers import RegisterSerializer
from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer, CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'
    

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer