from wolfpack.models import ProductBacklogItem, Project

from . import ProjectDao


def getAllItem():
    allItem = ProductBacklogItem.objects.all()
    return allItem

def getPbiByStatus(projectId, status):
    return ProductBacklogItem.objects.filter(projectId=projectId).filter(status=status)

def getPbiNotInStatus(projectId, status):
    return ProductBacklogItem.objects.filter(projectId=projectId).exclude(status=status)

def getItemById(pid):
    return ProductBacklogItem.objects.get(pk=pid)

def insert(size, priority, status, userStory, projectId):
    project = ProjectDao.getProjectById(projectId)
    pbi = ProductBacklogItem(
        size=size,
        priority=priority,
        status=status,
        userStory=userStory,
        projectId=project
    )
    pbi.save()
    return pbi.pk


def deleteById(pid):
    pbi = getItemById(pid)
    pbi.delete()


def updateById(pid, size=None, priority=None, status=None, userStory=None, projectId=None):
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

    pbi.save()


def viewAllCurrentPbi():
    return ProductBacklogItem.objects.all().exclude(status='done')


def viewAllDonePbi():
    return ProductBacklogItem.objects.all().filter(status='done')