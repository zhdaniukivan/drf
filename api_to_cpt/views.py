from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
