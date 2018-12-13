from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

flag = 0

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
            global flag
            flag = 1
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

def profile(request):
    return render(request,'registration/profile.html',{})