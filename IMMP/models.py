from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=120)
    skill_req = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    doc = models.FileField(upload_to='IMMP/projects/')

    def __str__(self):
        return self.project_name
