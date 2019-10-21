from django.db import models


# Create your models here.
# don't need to create primary key as django will create it for us

class User(models.Model):
    name = models.CharField()


class Project(models.Model):
    title = models.CharField()
    description = models.CharField()
    scrumMaster = models.ForeignKey(User)
