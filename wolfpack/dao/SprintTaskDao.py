from django.shortcuts import get_object_or_404

from wolfpack.models import SprintTask

from . import SprintBacklogDao, UserDao, ProductBacklogItemDao
from wolfpack.Enum import UserRoleEnum, SprintTaskStatusEnum


def getSprintTaskById(tid):
    return get_object_or_404(SprintTask, id=tid)


def insert(title, description, status, effortHours, developerId, sprintId, pbiId):
    task = SprintTask(
        title=title,
        description=description,
        status=status,
        effortHours=effortHours,
        owner=UserDao.getUserById(developerId, UserRoleEnum.DEVELOPER),
        sprintId=SprintBacklogDao.getSprintBacklogById(sprintId),
        pbiId=ProductBacklogItemDao.getItemById(pbiId)
    )
    task.save()
    return task.pk


def updateById(tid, title=None, description=None, status=None, effortHours=None, owner=None, sprintId=None, pbiId=None):
    task = getSprintTaskById(tid)
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if status is not None:
        task.status = status
    if effortHours is not None:
        task.effortHours = effortHours
    if owner is not None:
        developer=UserDao.getUserById(owner, UserRoleEnum.DEVELOPER)
        task.owner = developer
    if sprintId is not None:
        task.sprintId = sprintId
    if pbiId is not None:
        task.pbiId = pbiId

    task.save()

def getSprintTasksByPbiId(pbiId):
    return SprintTask.objects.all().filter(pbiId=pbiId)

def deleteById(tid):
    task = getSprintTaskById(tid)
    task.delete()


def viewAllTodoTask():
    return SprintTask.objects.all().filter(status=SprintTaskStatusEnum.TO_DO)


def viewAllInprogressTask():
    return SprintTask.objects.all().filter(status=SprintTaskStatusEnum.IN_PROGRESS)


def viewAllDoneTask():
    return SprintTask.objects.all().filter(status=SprintTaskStatusEnum.DONE)


def getTaskByStatus(sprintId, status):
    sprint = SprintBacklogDao.getSprintBacklogById(sprintId)
    return SprintTask.objects.all().filter(sprintId=sprint, status=status)
