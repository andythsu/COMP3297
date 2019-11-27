from django.shortcuts import render

from wolfpack.Enum import UserRoleEnum
from wolfpack.dao import ProjectDao, UserDao

def index(request):
    userId = int(request.GET['id'])
    userRole = int(request.GET['role'])
    projectId = int(request.GET['projectId'])

    success = True

    if userRole == UserRoleEnum.SCRUM_MASTER.value:
        # update project object
        ProjectDao.updateById(pid=projectId, scrumMaster=userId)
    elif userRole == UserRoleEnum.DEVELOPER.value:
        # check if the developer has active project
        developer = UserDao.getUserById(pid=userId, role=UserRoleEnum.DEVELOPER)

        # if the developer has active project, he/she cannot take more projects
        if developer.projectId is not None:
            success = False
        else:
            # update developer project
            UserDao.updateById(userId, UserRoleEnum.DEVELOPER, projectId=projectId)
    else:
        raise Exception("user role is not scrum master or developer")

    context = {
        'success': success
    }
    return render(request, 'AcceptInvite.html', context)
