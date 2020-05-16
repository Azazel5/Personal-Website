from PIL import Image
from django.db import models

class SkillModel(models.Model):
    skill = models.CharField(max_length=255)
    years_spent = models.IntegerField()

    def __str__(self):
        return self.skill

class ProjectModel(models.Model):
    project_name = models.CharField(max_length=255)
    project_type = models.ManyToManyField('SkillModel')
    project_description = models.TextField()
    github_url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='proj_images')

    def __str__(self):
        return self.project_name

    # Image resizing done to make everything standard in the home page. 
    def save(self, *args, **kwargs):
        super(ProjectModel, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = img.resize((900, 650), Image.ANTIALIAS)
        img.save(self.image.path)

