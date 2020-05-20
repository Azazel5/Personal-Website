from PIL import Image
from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'

    def __str__(self):
        return self.category_name

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_to_read = models.IntegerField(null=True)
    categories = models.ManyToManyField('Categories')
    date_posted = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blogImages/', null=True)

    class Meta: 
        verbose_name = 'blog'
    
    def __str__(self):
        return self.title
