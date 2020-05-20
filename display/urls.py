from django.urls import path
from .views import (
    HomeView,
    BlogView, 
    BlogDetailView, 
    BlogCreateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='detail'), 
    path('blog/create/', BlogCreateView.as_view(), name='create')
]
