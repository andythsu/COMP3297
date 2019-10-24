from django.urls import path

from . import views
from .dao import ProductBacklogItemDao

app_name = 'wolfpack'


urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('details/<int:id>', views.details, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),

    # button actions
]
