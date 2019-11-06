from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .Enum import SprintTaskStatusEnum

from .models import SprintTask

from .dao import ProjectDao, SprintBacklogDao, SprintTaskDao

def insert(request, proId, sprintId):
    if request.method == 'POST':
        sprintTaskId = SprintTaskDao.insert(
            title =request.POST['title'],
            pbiId =request.POST['corpbi'],
            effortHours =request.POST['effortHours'],
            status = 0,
            owner = request.POST['owner'],
            description = request.POST['description'],
            sprintId =sprintId
        )
        messages.success(request, 'sprint task added : %s' % sprintTaskId)
        return redirect(reverse('wolfpack:sprint_detail', args=[proId,sprintId]))
    else:
        context = {
            'projectId': proId,
            'sprintId': sprintId
        }
        return render(request, 'SprintTaskAdd.html', context)


def index(request, proId, sprintId):
    pro = ProjectDao.getProjectById(proId)
    sprint = SprintBacklogDao.getSprintBacklogById(sprintId)
    tasks = SprintTaskDao.getTaskByStatus(proId, sprintId, status=SprintTaskStatusEnum.TO_DO.value)
    tasks2 = SprintTaskDao.getTaskByStatus(proId, sprintId, status=SprintTaskStatusEnum.IN_PROGRESS.value)
    tasks3 = SprintTaskDao.getTaskByStatus(proId, sprintId, status=SprintTaskStatusEnum.DONE.value)

    modifiedTask=[]
    modifiedTask2 = []
    modifiedTask3 = []

    for task in tasks:
        modifiedTask.append({
            'task': task,
        })

    for task in tasks2:
        modifiedTask.append({
            'task': task,
        })

    for task in tasks3:
        modifiedTask.append({
            'task': task,
        })

    context = {
        'pro': pro,
        'sprint':sprint,
        'tasks': modifiedTask,
        'tasks2': modifiedTask2,
        'tasks3': modifiedTask3
    }
    return render(request, 'SprintBacklogDetail.html', context)