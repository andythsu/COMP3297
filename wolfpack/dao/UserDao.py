from wolfpack.models import User
from wolfpack.models import ProductOwner
from wolfpack.models import Developer
from wolfpack.models import ScrumMaster


def getUserById(pid, role):
    if role == 'PO':
        return ProductOwner.objects.get(pid)
    elif role == 'SM':
        return ScrumMaster.objects.get(pid)
    else:
        return Developer.objects.get(pid)


def insert(name, role, projectId):
    if role == 'PO':
        user = ProductOwner(
            name=name,
            role=role,
            projectId=projectId
        )
        user.save()
        return user.userId
    elif role == 'SM':
        user = ScrumMaster(
            name=name,
            role=role,
            projectId=projectId
        )
        user.save()
        return user.userId
    else:
        user = Developer(
            name=name,
            role=role,
            projectId=projectId
        )
        user.save()
        return user.userId


def deleteById(pid, role):
    user = getUserById(pid, role)
    user.delete()

def getUserProject(userId):
    pass


def updateById(pid, name=None, role=None, projectId=None):
    user = getUserById(pid, role)
    if name is not None:
        user.name = name

    if role is not None:
        user.role = role

    if projectId is not None:
        user.projectId = projectId

    user.save()