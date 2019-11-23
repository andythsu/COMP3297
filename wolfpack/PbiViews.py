from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .Enum import PbiStatusEnum

from .models import ProductBacklogItem

from .dao import ProductBacklogItemDao, ProjectDao, SprintBacklogDao, SprintTaskDao


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
        'proId': proId,
        'pbi': pbi,
        'pbiStatusInString': PbiStatusEnum.getNameByValue(pbi.status)
    }
    return render(request, 'PbiDetail.html', context)


def update(request, proId, pbiId):
    pbi = ProductBacklogItemDao.getItemById(pid=pbiId)
    if request.method == 'POST':
        userStory = ProductBacklogItemDao.getItemById(pbiId).userStory
        ProductBacklogItemDao.updateById(pbiId,
                                         size=request.POST['size'],
                                         priority=request.POST['priority'],
                                         status=request.POST['status'],
                                         userStory=request.POST['userStory'])
        messages.success(request, 'PBI Updated : %s' % userStory)
        return redirect(reverse('wolfpack:get_project_pbis', args=[proId]))
    else:
        context = {
            'pbi': pbi,
            'proId': proId
        }
    return render(request, 'PbiUpdate.html', context)


def delete(request, proId, pbiId):
    if request.method == 'POST':
        userStory = ProductBacklogItemDao.getItemById(pbiId).userStory
        ProductBacklogItemDao.deleteById(pbiId)
        messages.success(request, 'Pbi Deleted : %s' % userStory)

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
        if (eachPbi.status==1):
            status="In progress"
        if (eachPbi.status==0):
            status="Not started"
        if (eachPbi.status == 3):
            status = "Not finished"
        modifiedPbi2.append({
            'pbi': eachPbi,
            'cumusize': pbis2_cumu,
            # Update 3Nov 0145: Passes the cumulative size of each PBI
            'statusInString': status
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
    sprints = SprintBacklogDao.getAllSprintsByProjectId(proId)
    sprintList = []
    for sprint in sprints:
        sprintList.append({
            'sprint': sprint,
        })
    if request.method == 'POST':
        ProductBacklogItemDao.updateById(pbiId,
                                         sprintId=request.POST['sprintId'],
                                         status=1)

#        sprintTaskId = SprintTaskDao.insert(
#            title=request.POST['title'],
#            pbiId=pbiId,
#            effortHours=request.POST['effortHours'],
#            status=1,
#            developerId=request.POST['owner'],
#            description=request.POST['description'],
#            sprintId=request.POST['sprintId']
#        )

        messages.success(request, 'PBI Added to Sprint')
        context = {
            'pbi': pbi,
            'pbiStatusInString':PbiStatusEnum.getNameByValue(pbi.status)
        }
        return render(request, 'PbiDetail.html', context)
    else:
        context = {
            'pbi': pbi,
            'proId': proId,
            'pro': pro,
            'sprints': sprintList
        }
    return render(request, 'PbiAddToSprint.html', context)


def rejectFromSprint(request, proId, pbiId):
    sprintId = ProductBacklogItemDao.getItemById(pbiId).sprintId
    reject = True
    tasks = SprintTaskDao.getSprintTasksByPbiId(pbiId)
    if tasks:
        for task in tasks:
            if task.status>0:
                reject = False
    if reject:
        ProductBacklogItemDao.rejectPbi(pbiId)
        messages.success(request, 'PBI reject successfully')
        return redirect(reverse('wolfpack:sprint_detail', args=[proId, sprintId]))
    else:
        messages.info(request, 'PBI has started task(s), cannot be rejected')
        return redirect(reverse('wolfpack:sprint_detail', args=[proId, sprintId]))