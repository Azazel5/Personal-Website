from rest_framework import mixins
from rest_framework import viewsets

from .models import BlogModel 
from .serializers import BlogSerializer

class BlogViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):

    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class CreateViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer    
