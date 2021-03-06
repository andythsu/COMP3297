from django.urls import path

from . import PbiViews
from . import ProjectViews
from . import SprintBacklogViews
from . import SprintDetailViews
from . import AcceptInviteViews
from . import AuthViews

app_name = 'wolfpack'

urlpatterns = [
    path('', AuthViews.login, name='login'),
    path('user', AuthViews.info, name='userInfo'),
    path('logout', AuthViews.logout, name='logout'),
    path('index_project', ProjectViews.index, name='index_project'),
    path('add_project', ProjectViews.insertProject, name='add_project'),
    path('delete_project/<int:proId>', ProjectViews.deleteProject, name='delete_project'),
    # path('project_invite_developer/<int:proId>', ProjectViews.inviteDeveloper, name='project_invite_developer'),
    # path('project_invite_scrumMaster/<int:proId>', ProjectViews.inviteScrumMaster, name='project_invite_scrumMaster'),
    path('project/<int:proId>/pbi/insert', PbiViews.insert, name='insert'),
    path('project/<int:proId>/pbi/<int:pbiId>/details', PbiViews.details, name='detail'),
    path('project/<int:proId>/pbi', PbiViews.getProjectPbis, name='get_project_pbis'),
    path('project/<int:proId>/pbi/<int:pbiId>/delete', PbiViews.delete, name='delete'),
    path('project/<int:proId>/pbi/<int:pbiId>/update', PbiViews.update, name='update'),
    path('project/<int:proId>/pbi/<int:pbiId>/addToSprint', PbiViews.addToSprint, name='addToSprint'),
    path('project/<int:proId>/pbi/<int:pbiId>/reject', PbiViews.rejectFromSprint, name='rejectFromSprint'),
    path('project/<int:proId>/sprint', SprintBacklogViews.index, name='index_sprint'),
    path('project/<int:proId>/sprint/insert', SprintBacklogViews.insert, name='add_sprint'),
    path('project/<int:proId>/sprint/<int:sprintId>/details', SprintDetailViews.index, name='sprint_detail'),
    path('project/<int:proId>/sprint/<int:sprintId>/update', SprintBacklogViews.update, name='sprint_update'),
    path('project/<int:proId>/sprint/<int:sprintId>/start', SprintBacklogViews.start, name='sprint_start'),
    path('project/<int:proId>/sprint/<int:sprintId>/close', SprintBacklogViews.close, name='sprint_close'),
    path('project/<int:proId>/sprint/<int:sprintId>/insert', SprintDetailViews.insert, name='add_task'),
    path('project/<int:proId>/sprint/<int:sprintId>/deleteTask/<int:taskId>', SprintDetailViews.delete, name='delete_t'),
    path('project/<int:proId>/sprint/<int:sprintId>/updateTask/<int:taskId>', SprintDetailViews.update, name='update_t'),
    path('project/<int:proId>/sprint/<int:sprintId>/finishTask/<int:taskId>', SprintDetailViews.finish, name='finish_t'),
    path('accept_invitation', AcceptInviteViews.index, name="accept_invite")
]

