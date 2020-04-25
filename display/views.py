from django.shortcuts import render
from .models import ProjectModel
from django.views.generic import TemplateView
from django.views.generic.list import ListView

class HomeView(ListView):
    model = ProjectModel
    template_name = 'display/index.html'
    context_object_name = 'projects'

class BlogView(TemplateView):
    template_name = 'display/blog.html'
    
