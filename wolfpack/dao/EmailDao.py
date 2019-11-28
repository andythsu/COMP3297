from django.core.mail import send_mail
from django.conf import settings
from wolfpack.dao import UserDao, ProjectDao
from wolfpack.Enum import UserRoleEnum


def sendEmail(scrumMaster, developers, projectId):
    project = ProjectDao.getProjectById(pid=projectId)
    subject = "project invitation"
    message_sm = "You have been invited to be the scrum master for project " + project.title
    from_email = settings.EMAIL_HOST_USER
    # send to scrum master
    sm = UserDao.getUserById(pid=scrumMaster, role=UserRoleEnum.SCRUM_MASTER)
    developers = [UserDao.getUserById(pid=developer, role=UserRoleEnum.DEVELOPER) for developer in developers]

    sendToSM(sm, subject, from_email, project)
    sendToDev(developers, subject, from_email, project)

    send_mail(
        subject,
        message_sm,
        from_email,
        [sm.email]
    )


def sendToSM(scrumMaster, subject, from_email, project):
    link = "localhost:8000/accept_invitation?id="+str(scrumMaster.id)+"&role="+str(scrumMaster.role)+"&projectId="+str(project.id)
    message = "You have been invited to be the scrum master for project " + project.title
    message += "\n"
    message += "Click on the button or copy the link below to accept invitation."
    message += "\n"
    message += "<a href="+link+">Accept</a>"
    message += "\n"
    message += "link: " + link
    send_mail(
        subject,
        message,
        from_email,
        [scrumMaster.email],
        fail_silently=False
    )

def sendToDev(developers, subject, from_email, project):
    message_dev = "You have been invited to be the developer for project " + project.title
    message_dev += "\n"
    message_dev += "Click on the button or copy the link below to accept invitation."
    message_dev += "\n"

    for developer in developers:
        link = "localhost:8000/accept_invitation?id=" + str(developer.id) + "&role=" + str(developer.role) + "&projectId=" + str(project.id)
        message_dev += "<a href="+link+">Accept</a>"
        message_dev += "\n"
        message_dev += "link: " + link
        send_mail(
            subject,
            message_dev,
            from_email,
            [developer.email],
            fail_silently=False
        )
