from django.urls import path

from . import PbiViews
from . import ProjectViews

app_name = 'wolfpack'

urlpatterns = [
    path('', ProjectViews.index, name='index'),
    path('project/insert/<int:projectId>', PbiViews.insert, name='insert'),
    path('index_project', ProjectViews.index, name='index_project'),
    path('add_project', ProjectViews.insertProject, name='add_project'),
    path('delete_project/<int:id>', ProjectViews.deleteProject, name='delete_project'),
    path('project/details/<int:id>', PbiViews.details, name='detail'),
    path('project/<int:id>', PbiViews.getProjectPbis, name='get_project_pbis'),
    path('project/delete/<int:id>', PbiViews.delete, name='delete'),
    path('project/update/<int:id>', PbiViews.update, name='update'),

    # button actions
]
