from django.shortcuts import render
from .models import ProjectList, AwardList, ActivitiesList

# Create your views here.
def index(request):
    project_list = ProjectList.objects.all()
    award_list = AwardList.objects.all()
    activities_list = ActivitiesList.objects.all()

    context = {
        'project_list' : project_list, 
        'award_list' : award_list, 
        'activities_list' : activities_list
    }
    return render(request, 'index.html', context)

def detail(request, project_pk):
    project = ProjectList.objects.get(pk=project_pk)
    context = {
        'project_obj' : project
    }
    return render(request, 'detail.html', context)