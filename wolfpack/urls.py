from django.urls import path

from . import PbiViews
from . import ProjectViews
from . import SprintBacklogViews
from . import SprintDetailViews

app_name = 'wolfpack'

urlpatterns = [
    path('', ProjectViews.index, name='index'),
    path('index_project', ProjectViews.index, name='index_project'),
    path('add_project', ProjectViews.insertProject, name='add_project'),
    path('delete_project/<int:proId>', ProjectViews.deleteProject, name='delete_project'),
    path('project/<int:proId>/pbi/insert', PbiViews.insert, name='insert'),
    path('project/<int:proId>/pbi/<int:pbiId>/details', PbiViews.details, name='detail'),
    path('project/<int:proId>/pbi', PbiViews.getProjectPbis, name='get_project_pbis'),
    path('project/<int:proId>/pbi/<int:pbiId>/delete', PbiViews.delete, name='delete'),
    path('project/<int:proId>/pbi/<int:pbiId>/update', PbiViews.update, name='update'),
    path('project/<int:proId>/pbi/<int:pbiId>/addToSprint', PbiViews.addToSprint, name='addToSprint'),
    path('project/<int:proId>/sprint', SprintBacklogViews.index, name='index_sprint'),
    path('project/<int:proId>/sprint/insert', SprintBacklogViews.insert, name='add_sprint'),
    path('project/<int:proId>/sprint/<int:sprintId>/details', SprintDetailViews.index, name='sprint_detail'),
    path('project/<int:proId>/sprint/<int:sprintId>/update', SprintBacklogViews.update, name='sprint_update'),
    path('project/<int:proId>/sprint/<int:sprintId>/close', SprintBacklogViews.close, name='sprint_close'),
    path('project/<int:proId>/sprint/<int:sprintId>/insert', SprintDetailViews.insert, name='add_task'),
    path('project/<int:proId>/sprint/<int:sprintId>/deleteTask/<int:taskId>', SprintDetailViews.delete, name='delete_t'),
    path('project/<int:proId>/sprint/<int:sprintId>/updateTask/<int:taskId>', SprintDetailViews.update, name='update_t'),
    path('project/<int:proId>/sprint/<int:sprintId>/finishTask/<int:taskId>', SprintDetailViews.finish, name='finish_t')
]

