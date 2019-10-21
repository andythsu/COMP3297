from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home_page'),
    # button actions
    path('infoBtnOnClick/', views.infoBtnOnClick, name='infoBtnOnClick')
]
