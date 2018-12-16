from django.db import models

class product(models.Model):
    objects=models.Manager()
    username = models.CharField(max_length=225, blank=True)
    project_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to="projects/uploads/")
    
    def __str__(self):
        return self.project_name