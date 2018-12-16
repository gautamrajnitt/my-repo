from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

import app

def index(request):
    return render(request,'IMMP/index.html',{})

def projects(request):
    return render(request,'IMMP/projects.html',{})

def members(request):
    return render(request,'IMMP/members.html',{})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{
        'form':form
    })

def contact(request):
    return render(request,'IMMP/contact.html',{})

def team(request):
    return render(request,'IMMP/team.html',{})

def faq(request):
    return render(request,'IMMP/faq.html',{})

@login_required
def profile(request):
    return render(request,'registration/profile.html',{})

@login_required
def newproject(request):
    return render(request, 'IMMP/newproject.html', {})