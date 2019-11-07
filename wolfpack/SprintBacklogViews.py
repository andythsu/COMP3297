from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .dao import ProjectDao, SprintBacklogDao

from wolfpack.Enum import SprintStatusEnum


def index(request, proId):
    pro = ProjectDao.getProjectById(proId)
    sprints = SprintBacklogDao.getAllSprints(proId)
    sprintList = []
    for sprint in sprints:
        sprintList.append({
            'sprint': sprint,
        })
    context = {
        'pro': pro,
        'sprints': sprintList
    }
    return render(request, 'SprintIndex.html', context)


def insert(request, proId):
    if request.method == 'POST':
        sprintBacklogId = SprintBacklogDao.insert(
            name=request.POST['name'],
            startDate=request.POST['startDate'],
            endDate=request.POST['endDate'],
            maxHours=request.POST['maxHours'],
            status=SprintStatusEnum.IN_PROGRESS,  # this will restrict user from editing the sprint backlog detail after they create it
            projectId=proId
        )
        messages.success(request, 'sprint backlog added : %s' % sprintBacklogId)
        return redirect(reverse('wolfpack:index_sprint', args=[proId]))
    else:
        context = {
            'projectId': proId
        }
        return render(request, 'SprintBacklogAdd.html', context)


def update(request, proId, sprintId):
    sprint = SprintBacklogDao.getSprintBacklogById(sprintId)
    if request.method == 'POST':
        SprintBacklogDao.updateById(sprintId,
                                    name=request.POST['name'],
                                    startDate=request.POST['startDate'],
                                    endDate=request.POST['endDate'],
                                    maxHours=request.POST['maxHours'])
        messages.success(request, 'PBI Updated : %s' % sprintId)
        return redirect(reverse('wolfpack:index_sprint', args=[proId]))
    else:
        context = {
            'sprint': sprint,
            'proId': proId
        }
    return render(request, 'SprintUpdate.html', context)
