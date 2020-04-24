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
    github_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='proj_images')

    def __str__(self):
        return self.project_name