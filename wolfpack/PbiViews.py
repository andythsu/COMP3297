from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .Enum import PbiStatusEnum

from .models import ProductBacklogItem

from .dao import ProductBacklogItemDao, ProjectDao, SprintBacklogDao


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
    pbi = list(ProductBacklogItemDao.getPbiByStatus(projectId=proId, status=PbiStatusEnum.DONE.value))
    pbi2 = list(ProductBacklogItemDao.getPbiNotInStatus(projectId=proId, status=PbiStatusEnum.DONE.value))
    #Update 3Nov 0005: Convert QuerySet to List so that can be sorted

    pbi.sort(key=lambda x: x.priority)
    pbi2.sort(key=lambda x: x.priority)
    #Update 3Nov 0005: Sort according to priority

    modifiedPbi = []
    modifiedPbi2 = []

    pbis_cumu=0
    pbis2_cumu=0
    # Update 3Nov 0145: Have variable to store cumulative sizes

    for eachPbi in pbi:
        pbis_cumu+=eachPbi.size
        modifiedPbi.append({
            'pbi': eachPbi,
            'cumusize': pbis_cumu,
            # Update 3Nov 0145: Passes the cumulative size of each PBI
            'statusInString': PbiStatusEnum.getNameByValue(eachPbi.status)
        })

    for eachPbi in pbi2:
        pbis2_cumu += eachPbi.size
        modifiedPbi2.append({
            'pbi': eachPbi,
            'cumusize': pbis2_cumu,
            # Update 3Nov 0145: Passes the cumulative size of each PBI
            'statusInString': PbiStatusEnum.getNameByValue(eachPbi.status)
        })

    context = {
        'pro': pro,
        'pbis': modifiedPbi,
        'pbis2': modifiedPbi2
    }
    return render(request, 'PbiIndex.html', context)

def addToSprint(request, proId, pbiId):
    pbi = ProductBacklogItemDao.getItemById(pid=pbiId)
    pro = ProjectDao.getProjectById(proId)
    sprints = SprintBacklogDao.getAllSprints(proId)
    sprintList = []
    for sprint in sprints:
        sprintList.append({
            'sprint': sprint,
        })
    if request.method == 'POST':
        ProductBacklogItemDao.updateById(pbiId,
                                         sprintId=request.POST['sprintId'],
                                         status=1)
        messages.success(request, 'PBI Added to Sprint : %s' % pbi.sprintId)
        return redirect(reverse('wolfpack:get_project_pbis', args=[proId]))
    else:
        context = {
            'pbi': pbi,
            'proId': proId,
            'pro': pro,
            'sprints': sprintList
        }
    return render(request, 'PbiAddToSprint.html', context)