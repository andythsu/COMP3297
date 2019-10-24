from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    class Meta:
        abstract = True


class ProductOwner(User):
    projectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=False, null=False)


class ScrumMaster(User):
    projectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=True, null=True)


class Developer(User):
    projectId = models.ForeignKey('Project', on_delete=models.DO_NOTHING, blank=True, null=True)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    scrumMaster = models.IntegerField()


class ProductBacklogItem(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.IntegerField()
    priority = models.IntegerField()
    status = models.CharField(max_length=10)
    userStory = models.TextField()
    projectId = models.IntegerField();
    #I changed the projectID because it gives errors
    # This attribute is for further implementation.
    # sprintID = models.ForeignKey('Sprint', blank=True, null=True)
