from rest_framework import routers
from django.urls import path, include 

from .views import (
    BlogViewSet,
    CreateViewSet
)

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet, basename='blogs')
router.register('create', CreateViewSet, basename='create')

urlpatterns = [
    path('', include(router.urls)), 
]
