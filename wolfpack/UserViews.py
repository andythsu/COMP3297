from django.shortcuts import redirect, render, get_object_or_404

from wolfpack.Enum import UserRoleEnum
from wolfpack.dao import EmailDao, AuthDao
from .models import Project
from django.contrib import messages
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        isLogin = AuthDao.login(request, email, password, int(role))
        if isLogin:
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials! Please enter your email and password again.')
            return redirect(reverse('wolfpack:login'))
    else:
        return render(request, 'login.html')