from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'IMMP/index.html',{})

def projects(request):
    return render(request,'IMMP/projects.html',{})

def members(request):
    return render(request,'IMMP/members.html',{})

def login(request):
    return render(request,'IMMP/login.html',{})

def signup(request):
    return render(request,'IMMP/signup.html',{})

def contact(request):
    return render(request,'IMMP/contact.html',{})

def team(request):
    return render(request,'IMMP/team.html',{})

def faq(request):
    return render(request,'IMMP/faq.html',{})

