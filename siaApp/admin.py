from django.contrib import admin
from .models import ProjectList, AwardList, ActivitiesList

# Register your models here.
admin.site.register(ProjectList)
admin.site.register(AwardList)
admin.site.register(ActivitiesList)