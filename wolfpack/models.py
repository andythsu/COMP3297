from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ProductOwner(User):
    projectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=False, null=False)


class ScrumMaster(User):
    projectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=True, null=True)


class Developer(User):
    projectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=True, null=True)


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    scrumMaster = models.ForeignKey('ScrumMaster', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductBacklogItem(models.Model):
    size = models.IntegerField()
    priority = models.IntegerField()
    status = models.CharField(max_length=10)
    userStory = models.TextField()
    projectId = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.pk

    # I changed the projectID because it gives errors (Sam)
    # projectId = models.IntegerField()

    # This attribute is for further implementation.
    # sprintID = models.ForeignKey('Sprint', blank=True, null=True)
