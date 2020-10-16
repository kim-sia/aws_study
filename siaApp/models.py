from django.db import models

# Create your models here.
class ProjectList(models.Model):
    proj_date = models.CharField(max_length = 30)
    proj_group = models.CharField(max_length = 30)
    proj_topic = models.TextField()
    proj_overview = models.TextField()
    proj_summary = models.TextField()