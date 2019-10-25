from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from django.http import HttpResponse

from .models import ProductBacklogItem
from .models import Project


def index(request):
    pbi = ProductBacklogItem.objects.all()[:10]
    context = {
        'pbis': pbi
    }
    return render(request, 'index.html', context)


def insert(request, id):
    if (request.method == 'POST'):
        pbi = ProductBacklogItem(
            size=request.POST['size'],
            priority=request.POST['priority'],
            status=request.POST['status'],
            userStory=request.POST['userStory'],
            projectId=id,
        )
        pbi.save()
        messages.success(request, 'Product Added : %s' % pbi.projectId)
        return redirect(reverse('wolfpack:project', args=[id]))
    else:
        context = {
            'id': id
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
        pbi.save()
        messages.success(request, 'Product Updated : %s' % pbi.projectId)
        return redirect(reverse('wolfpack:project', args=[pbi.projectId]))

    else:
        context = {
            'pbi': pbi,
        }
    return render(request, 'edit.html', context)



def delete(request, id):
    if request.method == 'POST':
        pbi = get_object_or_404(ProductBacklogItem, pk=id)
        messages.success(request, 'Product Deleted : %s' % pbi.projectId)
        pid = pbi.projectId
        pbi.delete()

    return redirect(reverse('wolfpack:project', args=[pid]))


def add_project(request):
    if (request.method == 'POST'):
        project = Project(
            title=request.POST['title'],
            description=request.POST['description'],
            scrumMaster=request.POST['scrumMaster'],
        )
        project.save()
        messages.success(request, 'Project Added : %s' % project.title)
        return redirect(reverse('wolfpack:index_project'))
    else:
        return render(request, 'add_project.html')


def index_project(request):
    pro = Project.objects.all()[:10]
    context = {
        'projects': pro
    }
    return render(request, 'index_project.html', context)

def project(request, id):
    pro = get_object_or_404(Project, pk=id)
    pbi2 = ProductBacklogItem.objects.filter(projectId=id, status="not done")
    pbi = ProductBacklogItem.objects.filter(projectId=id, status="done")
    context = {
        'pro': pro,
        'pbis': pbi,
        'pbis2': pbi2
    }
    return render(request, 'project.html', context)

def delete_project(request, id):
    if request.method == 'POST':
        pro = get_object_or_404(Project, pk=id)
        messages.success(request, 'Project Deleted : %s' % pro.title)
        pro.delete()
    return redirect(reverse('wolfpack:index_project'))

