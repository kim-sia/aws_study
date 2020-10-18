from django.shortcuts import render
from .models import ProjectList, AwardList, ActivitiesList

# Create your views here.
def index(request):
    project_list = ProjectList.objects.all()
    award_list = AwardList.objects.all()
    activities_list = ActivitiesList.objects.all()
    return render(request, 'index.html', {'project_list' : project_list, 'award_list' : award_list, 'activities_list' : activities_list})