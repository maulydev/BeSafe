from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer