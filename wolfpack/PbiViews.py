from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .Enum import PbiStatusEnum

from .models import ProductBacklogItem

from .dao import ProductBacklogItemDao, ProjectDao


# inserts pbi
def insert(request, proId):
    if request.method == 'POST':
        pbiId = ProductBacklogItemDao.insert(
            size=request.POST['size'],
            priority=request.POST['priority'],
            status=0,
            userStory=request.POST['userStory'],
            projectId=proId
        )
        messages.success(request, 'pbi added : %s' % pbiId)
        return redirect(reverse('wolfpack:get_project_pbis', args=[proId]))
    else:
        context = {
            'projectId': proId
        }
        return render(request, 'PbiAdd.html', context)


def details(request, proId, pbiId):
    pbi = ProductBacklogItemDao.getItemById(pbiId)
    context = {
        'pbi': pbi,
    }
    return render(request, 'PbiDetail.html', context)


def update(request, proId, pbiId):
    pbi = ProductBacklogItemDao.getItemById(pid=pbiId)
    if request.method == 'POST':
        ProductBacklogItemDao.updateById(pbiId,
                                         size=request.POST['size'],
                                         priority=request.POST['priority'],
                                         status=request.POST['status'],
                                         userStory=request.POST['userStory'])
        messages.success(request, 'PBI Updated : %s' % pbiId)
        return redirect(reverse('wolfpack:get_project_pbis', args=[proId]))
    else:
        context = {
            'pbi': pbi,
            'proId': proId
        }
    return render(request, 'PbiUpdate.html', context)


def delete(request, proId, pbiId):
    if request.method == 'POST':
        ProductBacklogItemDao.deleteById(pbiId)
        messages.success(request, 'Pbi Deleted : %s' % pbiId)

    return redirect(reverse('wolfpack:get_project_pbis', args=[proId]))


def getProjectPbis(request, proId):
    pro = ProjectDao.getProjectById(proId)
    pbi = ProductBacklogItemDao.getPbiByStatus(projectId=proId, status=PbiStatusEnum.DONE.value)
    pbi2 = ProductBacklogItemDao.getPbiNotInStatus(projectId=proId, status=PbiStatusEnum.DONE.value)

    modifiedPbi = []
    modifiedPbi2 = []

    for eachPbi in pbi:
        modifiedPbi.append({
            'pbi': eachPbi,
            'statusInString': PbiStatusEnum.getNameByValue(eachPbi.status)
        })

    for eachPbi in pbi2:
        modifiedPbi2.append({
            'pbi': eachPbi,
            'statusInString': PbiStatusEnum.getNameByValue(eachPbi.status)
        })

    context = {
        'pro': pro,
        'pbis': modifiedPbi,
        'pbis2': modifiedPbi2
    }
    return render(request, 'PbiIndex.html', context)
