from django.shortcuts import redirect, render, get_object_or_404

from wolfpack.Enum import UserRoleEnum
from .models import Project
from django.contrib import messages
from django.urls import reverse

from .dao import ProjectDao, UserDao

def index(request):
    projects = ProjectDao.getAllProjects()

    projectList = []
    for project in projects:
        projectList.append({
            'project': project,
            'scrumMaster': project.scrumMaster.name
        })

    context = {
        'projects': projectList
    }
    return render(request, 'ProjectIndex.html', context)

def insertProject(request):
    user = list(UserDao.getUserByRole(UserRoleEnum.SCRUM_MASTER))
    modifiedUser = []
    for eachUser in user:
        modifiedUser.append({
            'user': eachUser,
        })
    if request.method == 'POST':
        projectId = ProjectDao.insert(
            title=request.POST['title'],
            description=request.POST['description'],
            scrumMasterId=request.POST['scrumMaster']
        )
        messages.success(request, 'Project Added : %s' % request.POST['title'])
        return redirect(reverse('wolfpack:index_project'))
    else:
        context = {
            'users': modifiedUser
        }
        return render(request, 'add_project.html', context)

def deleteProject(request, proId):
    if request.method == 'POST':
        ProjectDao.deleteById(proId)
        messages.success(request, 'Project Deleted : %s' % proId)
    return redirect(reverse('wolfpack:index_project'))
