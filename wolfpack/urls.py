from django.urls import path

from . import views
from .dao import ProductBacklogItemDao
from .dao import ProjectDao

app_name = 'wolfpack'


urlpatterns = [
    path('', views.index_project, name='index'),
    path('project/insert/<int:id>', views.insert, name='insert'),
    path('index_project', views.index_project, name='index_project'),
    path('add_project', views.add_project, name='add_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),
    path('project/details/<int:id>', views.details, name='detail'),
    path('project/<int:id>', views.project, name='project'),
    path('project/delete/<int:id>', views.delete, name='delete'),
    path('project/update/<int:id>', views.update, name='update'),

    # button actions
]
