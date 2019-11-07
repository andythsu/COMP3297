from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .Enum import SprintTaskStatusEnum, PbiStatusEnum, UserRoleEnum
from .dao import ProjectDao, SprintBacklogDao, SprintTaskDao, ProductBacklogItemDao, UserDao


def insert(request, proId, sprintId):
    #pbi list
    pbi = list(ProductBacklogItemDao.getPbiByStatus(projectId=proId, status=PbiStatusEnum.IN_PROGRESS.value).filter(sprintId=sprintId))
    pbi.sort(key=lambda x: x.priority)
    modifiedPbi = []
    pbis_cumu=0
    for eachPbi in pbi:
        pbis_cumu+=eachPbi.size
        modifiedPbi.append({
            'pbi': eachPbi,
            'cumusize': pbis_cumu,
            # Update 3Nov 0145: Passes the cumulative size of each PBI
            'statusInString': PbiStatusEnum.getNameByValue(eachPbi.status)
        })
    #user list
    user = list(UserDao.getUserByRole(UserRoleEnum.DEVELOPER))
    modifiedUser = []
    for eachUser in user:
        modifiedUser.append({
            'user': eachUser,
        })
    #post function
    if request.method == 'POST':
        sprintTaskId = SprintTaskDao.insert(
            title=request.POST['title'],
            description=request.POST['description'],
            status=0,
            effortHours=request.POST['effortHours'],
            developerId=request.POST['owner'],
            sprintId=sprintId,
            pbiId=request.POST['corpbi']
        )
        pbiId = request.POST['corpbi']
        messages.success(request, 'sprint task added : %s' % sprintTaskId)
        return redirect(reverse('wolfpack:sprint_detail', args=[proId, sprintId]))
    else:
        context = {
            'projectId': proId,
            'sprintId': sprintId,
            'pbis': modifiedPbi,
            'users': modifiedUser
        }
        return render(request, 'SprintTaskAdd.html', context)


def index(request, proId, sprintId):
    pro = ProjectDao.getProjectById(proId)
    sprint = SprintBacklogDao.getSprintBacklogById(sprintId)
    tasks = SprintTaskDao.getTaskByStatus(sprintId, status=SprintTaskStatusEnum.TO_DO.value)
    tasks2 = SprintTaskDao.getTaskByStatus(sprintId, status=SprintTaskStatusEnum.IN_PROGRESS.value)
    tasks3 = SprintTaskDao.getTaskByStatus(sprintId, status=SprintTaskStatusEnum.DONE.value)

    modifiedTask = []
    modifiedTask2 = []
    modifiedTask3 = []

    notfinish_cumu=0
    done_cumu=0

    for task in tasks:
        notfinish_cumu+=task.effortHours
        modifiedTask.append({
            'task': task,
        })

    for task in tasks2:
        notfinish_cumu+=task.effortHours
        modifiedTask2.append({
            'task': task,
        })

    for task in tasks3:
        done_cumu+=task.effortHours
        modifiedTask3.append({
            'task': task,
        })

    context = {
        'pro': pro,
        'sprint': sprint,
        'tasks': modifiedTask,
        'tasks2': modifiedTask2,
        'tasks3': modifiedTask3,
        'notdone': notfinish_cumu,
        'done': done_cumu
    }
    return render(request, 'SprintBacklogDetail.html', context)

def delete(request, proId, sprintId, taskId):
    if request.method == 'POST':
        SprintTaskDao.deleteById(taskId)
        messages.success(request, 'Task Deleted : %s' % taskId)

    pro = ProjectDao.getProjectById(proId)
    sprint = SprintBacklogDao.getSprintBacklogById(sprintId)
    tasks = SprintTaskDao.getTaskByStatus(sprintId, status=SprintTaskStatusEnum.TO_DO.value)
    tasks2 = SprintTaskDao.getTaskByStatus(sprintId, status=SprintTaskStatusEnum.IN_PROGRESS.value)
    tasks3 = SprintTaskDao.getTaskByStatus(sprintId, status=SprintTaskStatusEnum.DONE.value)

    modifiedTask = []
    modifiedTask2 = []
    modifiedTask3 = []

    notfinish_cumu=0
    done_cumu=0

    for task in tasks:
        notfinish_cumu+=task.effortHours
        modifiedTask.append({
            'task': task,
        })

    for task in tasks2:
        notfinish_cumu+=task.effortHours
        modifiedTask2.append({
            'task': task,
        })

    for task in tasks3:
        done_cumu+=task.effortHours
        modifiedTask3.append({
            'task': task,
        })

    context = {
        'pro': pro,
        'sprint': sprint,
        'tasks': modifiedTask,
        'tasks2': modifiedTask2,
        'tasks3': modifiedTask3
    }
#    return redirect(reverse('wolfpack:index_project'))
    return render(request, 'SprintBacklogDetail.html', context)
