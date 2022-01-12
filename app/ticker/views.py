from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Tick
from .serializers import TickSerializer


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Tick.objects.all()
    serializer_class = TickSerializer

