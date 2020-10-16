from django.db import models

# Create your models here.
class ProjectList(models.Model):
    proj_date = models.CharField(max_length = 30)
    proj_group = models.CharField(max_length = 30)
    proj_topic = model.TextField()
    proj_overview = model.TextField()
    proj_summary = model.TextField()