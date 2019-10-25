from django.shortcuts import get_object_or_404

from wolfpack.models import ProductOwner
from wolfpack.models import Developer
from wolfpack.models import ScrumMaster

from . import ProjectDao

from wolfpack.Enum import UserRoleEnum


def getUserById(pid, role):
    if role == UserRoleEnum.PRODUCT_OWNER:
        return get_object_or_404(ProductOwner, id=pid)
    elif role == UserRoleEnum.SCRUM_MASTER:
        return get_object_or_404(ScrumMaster, id=pid)
    elif role == UserRoleEnum.DEVELOPER:
        return get_object_or_404(Developer, id=pid)
    else:
        raise Exception("user role doesn't exist in enum")


def insert(name, role, projectId):
    if role == 'PO':
        user = ProductOwner(
            name=name,
            role=role,
            projectId=ProjectDao.getProjectById(projectId)
        )
        user.save()
        return user.id
    elif role == 'SM':
        user = ScrumMaster(
            name=name,
            role=role,
            projectId=ProjectDao.getProjectById(projectId)
        )
        user.save()
        return user.id
    else:
        user = Developer(
            name=name,
            role=role,
            projectId=ProjectDao.getProjectById(projectId)
        )
        user.save()
        return user.id


def deleteById(pid, role):
    user = getUserById(pid, role)
    user.delete()


def getUserProject(userId):
    pass


def updateById(pid, role, name=None, projectId=None):
    user = getUserById(pid, role)
    if name is not None:
        user.name = name

    if role is not None:
        user.role = role

    if projectId is not None:
        user.projectId = ProjectDao.getProjectById(projectId)

    user.save()


def getScrumMasterNameByProjectId(projectId):
    try:
        return ScrumMaster.objects.get(projectId=projectId).name
    except:
        return ""
