from django.db import models

class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    name   = models.CharField(max_length=20)
    role   = models.CharField(max_length=20)
    class Meta:
        abstract = True

class ProductOwner(User):
    projectID  = models.ForeignKey('Project', on_delete=models.PROTECT, blank=False, null=False)

class ScrumMaster(User):
    projectID  = models.ForeignKey('Project', on_delete=models.PROTECT, blank=True, null=True)

class Developer(User):
    projectID  = models.ForeignKey('Project', on_delete=models.PROTECT, blank=True, null=True)

class Project(models.Model):
    projectID    = models.IntegerField(primary_key=True)
    title        = models.CharField(max_length=50)
    description  = models.TextField(blank=True,null=True)
    scrum_master = models.IntegerField()

class PBI(models.Model):
    ID         = models.IntegerField(primary_key=True)
    size       = models.IntegerField()
    priority   = models.IntegerField()
    status     = models.CharField(max_length=10)
    user_story = models.TextField()
    projectID  = models.ForeignKey('Project', on_delete=models.PROTECT, blank=False, null=False)
    # This attribute is for further implementation.
    # sprintID = models.ForeignKey('Sprint', blank=True, null=True)
