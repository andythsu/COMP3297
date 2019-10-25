from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from django.http import HttpResponse

from .models import ProductBacklogItem

from .dao import ProductBacklogItemDao


def index(request):
    pbi = ProductBacklogItemDao.getAllItem()
    # pbi = ProductBacklogItem.objects.all()[:10]
    context = {
        'pbis': pbi
    }
    return render(request, 'index.html', context)


def insert(request):
    if (request.method == 'POST'):
        pbiId = ProductBacklogItemDao.insert(
            size=request.POST['size'],
            priority=request.POST['priority'],
            status=request.POST['status'],
            userStory=request.POST['userStory'],
            projectId=request.POST['projectId'])
        # pbi = ProductBacklogItem(
        #     size=request.POST['size'],
        #     priority=request.POST['priority'],
        #     status=request.POST['status'],
        #     userStory=request.POST['userStory'],
        #     projectId=request.POST['projectId'],
        # )
        # pbi.save()
        messages.success(request, 'pbi added : %s' % pbiId)
        return redirect(reverse('wolfpack:index'))
    else:
        context = {
        }
        return render(request, 'add.html', context)


def details(request, id):
    pbi = get_object_or_404(ProductBacklogItem, pk=id)
    context = {
        'pbi': pbi,
    }
    return render(request, 'details.html', context)


def update(request, id):
    pbi = get_object_or_404(ProductBacklogItem, pk=id)
    if (request.method == 'POST'):
        pbi.size = request.POST['size']
        pbi.priority = request.POST['priority']
        pbi.status = request.POST['status']
        pbi.userStory = request.POST['userStory']
        pbi.projectId = request.POST['projectId']
        pbi.save()
        messages.success(request, 'Product Updated : %s' % pbi.projectId)
        return redirect(reverse('wolfpack:detail', args=[id]))

    else:
        context = {
            'pbi': pbi,
        }
    return render(request, 'edit.html', context)


def delete(request, id):
    if (request.method == 'POST'):
        pbi = get_object_or_404(ProductBacklogItem, pk=id)
        messages.success(request, 'Product Deleted : %s' % pbi.projectId)
        pbi.delete()

    return redirect(reverse('wolfpack:index'))
