from django.shortcuts import redirect, render, get_object_or_404

from wolfpack.Enum import UserRoleEnum
from wolfpack.dao import EmailDao
from .models import Project
from django.contrib import messages
from django.urls import reverse

from .dao import ProjectDao, UserDao, SessionDao
from .Enum import UserRoleEnum


def index(request):
    user = UserDao.getUserById(SessionDao.getUId(request), UserRoleEnum.getNameByValue(SessionDao.getURole(request)))
    projects = ProjectDao.getAllProjects()

    projectList = []
    for project in projects:
        projectList.append({
            'project': project,
            'scrumMaster': project.scrumMaster.name if project.scrumMaster is not None else ""
        })

    context = {
        'user': user,
        'projects': projectList
    }
    return render(request, 'ProjectIndex.html', context)


def insertProject(request):
    scrumMasters = list(UserDao.getUserByRole(UserRoleEnum.SCRUM_MASTER))
    availableDevelopers = list(UserDao.getAvailableDevelopers())
    modified_sm = []
    # modified_dev = []
    for scrumMaster in scrumMasters:
        modified_sm.append({
            'user': scrumMaster,
        })

    if request.method == 'POST':
        projectId = ProjectDao.insert(
            title=request.POST['title'],
            description=request.POST['description'],
        )
        EmailDao.sendEmail(request.POST['scrumMaster'], request.POST.getlist('developer'), projectId)
        messages.success(request, 'Project added : %s' % request.POST['title'])
        return redirect(reverse('wolfpack:index_project'))
    else:
        context = {
            'users': modified_sm,
            'availableDevelopers': availableDevelopers
        }
        return render(request, 'ProjectAdd.html', context)


def deleteProject(request, proId):
    if request.method == 'POST':
        project = ProjectDao.getProjectById(proId)
        ProjectDao.deleteById(proId)
        messages.success(request, 'Project deleted : %s' % project.title)
    return redirect(reverse('wolfpack:index_project'))


def inviteScrumMaster(request, proId):
    user = list(UserDao.getUserByRole(UserRoleEnum.SCRUM_MASTER))
    modifiedUser = []
    for eachUser in user:
        modifiedUser.append({
            'user': eachUser,
        })

    if request.method == 'POST':
        ##send email
        UserDao.invite(request.POST['scrumMaster'], proId)

        return redirect(reverse('wolfpack:index_project'))
    else:
        context = {
            'users': modifiedUser,
            'projectId': proId
        }
        return render(request, 'ProjectInviteScrumMaster.html', context)


def inviteDeveloper(request, proId):
    user = list(UserDao.getUserByRole(UserRoleEnum.DEVELOPER))
    modifiedUser = []
    for eachUser in user:
        modifiedUser.append({
            'user': eachUser,
        })

    if request.method == 'POST':
        ##send email
        UserDao.invite(request.POST['developer'], proId)

        return redirect(reverse('wolfpack:index_project'))
    else:
        context = {
            'users': modifiedUser,
            'projectId': proId
        }
        return render(request, 'ProjectInviteDeveloper.html', context)
