from django.shortcuts import render
from .models import Project

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio.html', context)

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)