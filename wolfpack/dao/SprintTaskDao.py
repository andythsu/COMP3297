from django.shortcuts import get_object_or_404

from wolfpack.models import SprintTask
from . import ProjectDao
from . import SprintBacklogDao


def getSprintTaskById(tid):
    return get_object_or_404(SprintTask, id=tid)


def insert(title, description, status, effortHours, owner, sprintId, pbiId):
    task = SprintTask(
        title=title,
        description=description,
        status=status,
        effortHours=effortHours,
        owner=owner,
        sprintId=SprintBacklogDao.getSprintBacklogById(sprintId),
        pbiId=ProjectDao.getProjectById(pbiId)
    )
    task.save()
    return task.pk


def updateById(tid, title=None, description=None, status=None, effortHours=None, owner=None, sprintId=None, pbiId=None):
    task = getSprintTaskById(tid)
    if title is not None:
        task.title = title
    if title is not None:
        task.description = description
    if title is not None:
        task.status = status
    if title is not None:
        task.effortHours = effortHours
    if title is not None:
        task.owner = owner
    if title is not None:
        task.sprintId = sprintId
    if title is not None:
        task.pbiId = pbiId

    task.save()


def deleteById(tid):
    task = getSprintTaskById(tid)
    task.delete()


def viewAllTodoTask():
    return SprintTask.objects.all().filter(status="todo")


def viewAllInprogressTask():
    return SprintTask.objects.all().filter(status="inprogress")


def viewAllDoneTask():
    return SprintTask.objects.all().filter(status='done')


def getTaskByStatus(projectId, sprintId, status):
    return []
