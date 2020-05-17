from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    class Meta: 
        verbose_name = 'blog'
    
    def __str__(self):
        return self.title