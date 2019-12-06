from wolfpack.models import ProductBacklogItem

from . import ProjectDao
from . import SprintBacklogDao


def getAllItem():
    allItem = ProductBacklogItem.objects.all()
    return allItem


def getItemById(pid):
    return ProductBacklogItem.objects.get(pk=pid)


def getPbiByStatus(projectId, status):
    return ProductBacklogItem.objects.filter(projectId=projectId).filter(status=status)


def getPbiNotInStatus(projectId, status):
    return ProductBacklogItem.objects.filter(projectId=projectId).exclude(status=status)


def getPbiBySprintId(projectId, sprintId):
    return ProductBacklogItem.objects.filter(projectId=projectId).filter(sprintId=sprintId)

def insert(size, priority, status, userStory, projectId):
    pbi = ProductBacklogItem(
        size=size,
        priority=priority,
        status=status,
        userStory=userStory,
        projectId=ProjectDao.getProjectById(projectId)
    )
    pbi.save()
    return pbi.userStory


def deleteById(pid):
    pbi = getItemById(pid)
    pbi.delete()


def updateById(pid, size=None, priority=None, status=None, userStory=None, projectId=None, sprintId=None):
    pbi = getItemById(pid)
    if size is not None:
        pbi.size = size

    if priority is not None:
        pbi.priority = priority

    if status is not None:
        pbi.status = status

    if userStory is not None:
        pbi.userStory = userStory

    if projectId is not None:
        pbi.projectId = projectId

    pbi.sprintId = SprintBacklogDao.getSprintBacklogById(sprintId)

    pbi.save()


def viewAllCurrentPbi():
    return ProductBacklogItem.objects.all().exclude(status=2)


def viewAllDonePbi():
    return ProductBacklogItem.objects.all().filter(status=2)


def rejectPbi(pid):
    updateById(pid, None, None, 0, None, None, None)

