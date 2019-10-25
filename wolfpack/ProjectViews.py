from django.shortcuts import redirect, render, get_object_or_404

from .models import Project
from django.contrib import messages
from django.urls import reverse

from .dao import ProjectDao

def index(request):
    pro = Project.objects.all()[:10]
    context = {
        'projects': pro
    }
    return render(request, 'index_project.html', context)

def insertProject(request):
    if request.method == 'POST':
        project = ProjectDao.insert(
            title=request.POST['title'],
            description=request.POST['description'],
            scrumMasterId=request.POST['scrumMaster']
        )
        messages.success(request, 'Project Added : %s' % request.POST['title'])
        return redirect(reverse('wolfpack:index_project'))
    else:
        return render(request, 'add_project.html')

def deleteProject(request, id):
    if request.method == 'POST':
        pro = get_object_or_404(Project, pk=id)
        messages.success(request, 'Project Deleted : %s' % pro.title)
        pro.delete()
    return redirect(reverse('wolfpack:index_project'))
