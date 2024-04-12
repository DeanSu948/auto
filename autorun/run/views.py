from django.shortcuts import render
from rest_framework import viewsets
from .models import FlashInfo
from .serializer import FlashInfoSerializer

# Create your views here.
class FlashInfoViewSet(viewsets.ModelViewSet):
    queryset = FlashInfo.objects.all()
    serializer_class = FlashInfoSerializer