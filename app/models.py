from django.db import models
import os
import datetime
from django.utils.timezone import utc

now = datetime.datetime.utcnow().replace(tzinfo=utc)

class product(models.Model):
    objects=models.Manager()
    username = models.CharField(max_length=225, blank=True)
    project_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to="projects/uploads/")
    
    def __str__(self):
        return self.project_name
    def filename(self):
        return os.path.basename(self.document.name)
     