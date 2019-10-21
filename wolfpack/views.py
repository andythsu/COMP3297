from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, "wolfpack.html",
                  context={
                      "name": "Andy"
                  })


def home(request):
    return render(request, "home.html")


def infoBtnOnClick(request):
    return HttpResponse('info button clicked')


def dangerBtnOnClick(request):
    print("")
