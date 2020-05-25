from django.urls import reverse
from django.core.mail import send_mail
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ProjectModel
from blog.models import BlogModel 


class HomeView(ListView):
    model = ProjectModel
    template_name = 'display/index.html'
    context_object_name = 'projects'

    # Handles the POST request for the contact me section
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f'Website Contact Form: {name}',
            f"""
            You\'ve received an email from your website contact form. Here are the details:
            name: {name}
            phone: {phone}
            email: {email}
            message: {message}
            """,
            email,
            ['subhanga2015@gmail.com'],
            fail_silently=False,
        )
        
        return redirect('home')

class BlogView(ListView):
    model = BlogModel
    template_name = 'display/blog.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'display/detail.html'
    context_object_name = 'blog_detail'

class BlogCreateRender(TemplateView):
    template_name = 'display/create.html'
