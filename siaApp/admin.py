from django.contrib import admin
from .models import ProjectList, AwardList

# Register your models here.
admin.site.register(ProjectList)
admin.site.register(AwardList)