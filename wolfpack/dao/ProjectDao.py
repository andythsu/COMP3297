from django.shortcuts import get_object_or_404

from wolfpack.models import Project

from . import UserDao


def getAllProjects():
    return Project.objects.all()

def getProjectById(pid):
    return get_object_or_404(Project, id=pid)


def insert(title, description):
    project = Project(
        title=title,
        description=description
    )
    project.save()
    return project.id


def deleteById(pid):
    project = getProjectById(pid)
    project.delete()


def updateById(pid, title=None, description=None, scrumMaster=None):
    project = getProjectById(pid)
    if title is not None:
        project.title = title

    if description is not None:
        project.description = description

    if scrumMaster is not None:
        project.scrumMaster = scrumMaster

    project.save()