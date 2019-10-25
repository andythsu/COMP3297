from wolfpack.models import Project, ProductBacklogItem


def getProjectById(pid):
    return Project.objects.get(pk=pid)


def insert(title, description, scrumMaster):
    project = ProductBacklogItem(
        title=title,
        description=description,
        scrumMaster=scrumMaster
    )
    project.save()
    return project.projectId


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