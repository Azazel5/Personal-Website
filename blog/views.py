from rest_framework import viewsets
from django.shortcuts import render

from .models import BlogModel 
from .serializers import BlogSerializer

class CRUDBlog(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
