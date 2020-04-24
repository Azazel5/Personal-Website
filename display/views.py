from django.shortcuts import render
from .models import ProjectModel
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'display/index.html'
    model = ProjectModel

class BlogView(TemplateView):
    template_name = 'display/blog.html'

