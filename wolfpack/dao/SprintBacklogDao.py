from django.shortcuts import get_object_or_404

from wolfpack.models import SprintBacklog
from . import ProjectDao


def getSprintBacklogById(pid):
    return get_object_or_404(SprintBacklog, id=pid)


def getAllSprints(projectId):
    return SprintBacklog.objects.all().filter(projectId=projectId)


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


def updateById(pid, name=None, startDate=None, endDate=None, maxHours=None, projectId=None):
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

    sprintBacklog.save()

