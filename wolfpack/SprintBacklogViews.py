from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .dao import SprintBacklogDao


def insert(request, proId):
    if request.method == 'POST':
        sprintBacklogId = SprintBacklogDao.insert(
            name=request.POST['name'],
            startDate=request.POST['startDate'],
            endDate=request.POST['endDate'],
            maxHours=request.POST['maxHours'],
            projectId=proId
        )
        messages.success(request, 'sprint backlog added : %s' % sprintBacklogId)
        return redirect(reverse('wolfpack:add_sprint', args=[proId]))
    else:
        context = {
            'projectId': proId
        }
        return render(request, 'SprintBacklogAdd.html', context)