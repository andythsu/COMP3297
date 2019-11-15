from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class ProductOwner(User):
    projectId = models.ForeignKey('Project', on_delete=models.SET_NULL, blank=False, null=True)


class ScrumMaster(User):
    # projectId = models.ForeignKey('Project', on_delete=models.SET_NULL, blank=True, null=True)
    pass


class Developer(User):
    projectId = models.ForeignKey('Project', on_delete=models.SET_NULL, blank=True, null=True)


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    scrumMaster = models.ForeignKey('ScrumMaster', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ProductBacklogItem(models.Model):
    size = models.IntegerField()
    priority = models.IntegerField()
    status = models.IntegerField()
    userStory = models.TextField()
    projectId = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)
    sprintId = models.ForeignKey('SprintBacklog', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class SprintBacklog(models.Model):
    name = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    maxHours = models.IntegerField()
    status = models.IntegerField()
    projectId = models.ForeignKey('Project', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return str(self.id)


class SprintTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField()
    effortHours = models.IntegerField()
    owner = models.ForeignKey('Developer', on_delete=models.CASCADE, blank=True, null=True)
    sprintId = models.ForeignKey('SprintBacklog', on_delete=models.CASCADE, blank=False, null=False)
    pbiId = models.ForeignKey('ProductBacklogItem', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return str(self.id)

    # I changed the projectID because it gives errors (Sam)
    # projectId = models.IntegerField()

    # This attribute is for further implementation.
    # sprintID = models.ForeignKey('Sprint', blank=True, null=True)
