from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from .models import Missionary, Update

from rest_framework import viewsets
from project.api.serializers import UserSerializer, MissionarySerializer, UpdateSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MissionaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Missionary.objects.all()
    serializer_class = MissionarySerializer

class UpdateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer