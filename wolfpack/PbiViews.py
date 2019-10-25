from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .Enum import PbiStatusEnum

from .models import ProductBacklogItem

from .dao import ProductBacklogItemDao, ProjectDao


# inserts pbi
def insert(request, projectId):
    if request.method == 'POST':
        pbiId = ProductBacklogItemDao.insert(
            size=request.POST['size'],
            priority=request.POST['priority'],
            status=0,
            userStory=request.POST['userStory'],
            projectId=projectId
        )
        messages.success(request, 'pbi added : %s' % pbiId)
        return redirect(reverse('wolfpack:get_project_pbis', args=[projectId]))
    else:
        context = {
            'projectId': projectId
        }
        return render(request, 'AddPbi.html', context)


def details(request, id):
    pbi = get_object_or_404(ProductBacklogItem, pk=id)
    context = {
        'pbi': pbi,
    }
    return render(request, 'details.html', context)


def update(request, id):
    pbi = ProductBacklogItemDao.getItemById(pid=id)
    if request.method == 'POST':
        ProductBacklogItemDao.updateById(id,
                                         size=request.POST['size'],
                                         priority=request.POST['priority'],
                                         status=request.POST['status'],
                                         userStory=request.POST['userStory'])
        messages.success(request, 'Product Updated : %s' % pbi.projectId)
        return redirect(reverse('wolfpack:get_project_pbis', args=[pbi.projectId]))
    else:
        context = {
            'pbi': pbi,
        }
    return render(request, 'UpdatePbi.html', context)


def delete(request, id):
    if request.method == 'POST':
        pbi = get_object_or_404(ProductBacklogItem, pk=id)
        pid = pbi.projectId
        pbi.delete()
        messages.success(request, 'Product Deleted : %s' % pbi.projectId)

    return redirect(reverse('wolfpack:get_project_pbis', args=[pid]))


def getProjectPbis(request, id):
    pro = ProjectDao.getProjectById(id)
    pbi = ProductBacklogItemDao.getPbiByStatus(projectId=id, status=PbiStatusEnum.DONE.value)
    pbi2 = ProductBacklogItemDao.getPbiNotInStatus(projectId=id, status=PbiStatusEnum.DONE.value)

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
    return render(request, 'ProductBacklogIndex.html', context)
