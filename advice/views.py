from rest_framework import viewsets
from .models import Advice
from .serializers import AdviceSerializer
from django_filters.rest_framework import DjangoFilterBackend



class AdviceViewSet(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profile__user__username']