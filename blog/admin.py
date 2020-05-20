from django.contrib import admin

from .models import BlogModel, Categories

admin.site.register(BlogModel)
admin.site.register(Categories)