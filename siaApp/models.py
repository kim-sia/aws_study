from django.db import models

# Create your models here.
class ProjectList(models.Model):
    proj_date = models.CharField(max_length = 30)
    proj_group = models.CharField(max_length = 30)
    proj_topic = models.TextField()
    proj_overview = models.TextField()
    proj_summary = models.TextField()

class AwardList(models.Model):
    award_date = models.CharField(max_length = 30)
    award_contest = models.TextField()
    award_host = models.TextField()
    award_result = models.TextField()

class ActivitiesList(models.Model):
    activities_group = models.TextField()
    activities_content = models.TextField()
    activities_duration = models.TextField()