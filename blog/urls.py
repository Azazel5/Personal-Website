from rest_framework import routers
from django.urls import path, include 

from .views import CRUDBlog

router = routers.DefaultRouter()
router.register('blogs', CRUDBlog)

urlpatterns = [
    path('', include(router.urls))
]
