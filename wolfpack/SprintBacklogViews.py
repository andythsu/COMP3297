from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .dao import ProjectDao, SprintBacklogDao, ProductBacklogItemDao, SprintTaskDao

from wolfpack.Enum import SprintStatusEnum, SprintTaskStatusEnum, PbiStatusEnum


def index(request, proId):
    pro = ProjectDao.getProjectById(proId)
    allSprintsInProject = SprintBacklogDao.getAllSprintsByProjectId(proId)
    activeSprints = []
    inactiveSprints = []
    for sprint in allSprintsInProject:
        if sprint.status == SprintStatusEnum.DONE.value:
            inactiveSprints.append({
                'sprint': sprint,
                'sprintStatus:': SprintStatusEnum.getNameByValue(sprint.status)
            })
        else:
            activeSprints.append({
                'sprint': sprint,
                'sprintStatus': SprintStatusEnum.getNameByValue(sprint.status)
            })

    context = {
        'pro': pro,
        'activeSprints': activeSprints,
        'inactiveSprints': inactiveSprints
    }
    return render(request, 'SprintIndex.html', context)


def insert(request, proId):
    if request.method == 'POST':
        sprintBacklogId = SprintBacklogDao.insert(
            name=request.POST['name'],
            startDate=request.POST['startDate'],
            endDate=request.POST['endDate'],
            maxHours=request.POST['maxHours'],
            status=SprintStatusEnum.IN_PROGRESS.value,
            # this will restrict user from editing the sprint backlog detail after they create it
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


def close(request, proId, sprintId):
    SprintBacklogDao.updateById(pid=sprintId, status=SprintStatusEnum.DONE.value)
    # if there are pbis with status not done at the end of sprint, set the pbi to unfinished
    # get all pbis in this sprint
    pbisInSprint = ProductBacklogItemDao.getPbiBySprintId(projectId=proId, sprintId=sprintId)
    for pbi in pbisInSprint:
        sprintTasks = SprintTaskDao.getSprintTasksByPbiId(pbi.id)
        tasksNotDone = list(filter(lambda sprintTask: sprintTask.status != SprintTaskStatusEnum.DONE.value, sprintTasks))
        if len(tasksNotDone) > 0:
            ProductBacklogItemDao.updateById(pid=pbi.id, status=PbiStatusEnum.NOT_FINISHED.value)
        else:
            ProductBacklogItemDao.updateById(pid=pbi.id, status=PbiStatusEnum.DONE.value)

    return redirect(reverse('wolfpack:index_sprint', args=[proId]))