from django.shortcuts import get_object_or_404

from wolfpack.models import SprintBacklog
from . import ProjectDao
from wolfpack.Enum import SprintStatusEnum


def getSprintBacklogById(pid):
    if pid is None:
        return None
    else:
        return get_object_or_404(SprintBacklog, id=pid)


def getLastSprintBacklog():
    if SprintBacklog.objects.exists():
        return SprintBacklog.objects.latest('id')
    else:
        return None


def getAllSprintsByProjectId(projectId):
    return SprintBacklog.objects.all().filter(projectId=projectId)


def getAllActiveSprintsByProjectId(projectId):
    return SprintBacklog.objects.all().filter(projectId=projectId).exclude(status=SprintStatusEnum.DONE.value)


def insert(name, startDate, endDate, maxHours, status, projectId):
    sprintBacklog = SprintBacklog(
        name=name,
        startDate=startDate,
        endDate=endDate,
        maxHours=maxHours,
        status=status,
        projectId=ProjectDao.getProjectById(projectId)
    )
    sprintBacklog.save()
    return sprintBacklog.pk


def deleteById(pid):
    sprintBacklog = getSprintBacklogById(pid)
    sprintBacklog.delete()


def updateById(pid, name=None, startDate=None, endDate=None, maxHours=None, projectId=None, status=None):
    sprintBacklog = getSprintBacklogById(pid)
    if name is not None:
        sprintBacklog.name = name

    if startDate is not None:
        sprintBacklog.startDate = startDate

    if endDate is not None:
        sprintBacklog.endDate = endDate

    if maxHours is not None:
        sprintBacklog.maxHours = maxHours

    if projectId is not None:
        sprintBacklog.projectId = projectId

    if status is not None:
        sprintBacklog.status = status

    sprintBacklog.save()

