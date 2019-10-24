from wolfpack.models import ProductBacklogItem


def getAllItem():
    allItem = ProductBacklogItem.objects.all()
    return allItem


def getItemById(pid):
    return ProductBacklogItem.objects.get(id=pid)


def insert(size, priority, status, userStory, projectId):
    pbi = ProductBacklogItem(
        size=size,
        priority=priority,
        status=status,
        userStory=userStory,
        projectId=projectId
    )
    pbi.save()
    return pbi.id


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
