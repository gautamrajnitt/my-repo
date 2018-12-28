from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import ProjectCreateForm
from django.core.files.storage import FileSystemStorage




def index2(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index2')
    else:
        form = UserCreationForm()
    return render(request,'IMMP/index2.html',{
        'form': form
    })

@login_required
def dashboard(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectCreateForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, "IMMP/dashboard.html", {
                'form' : form
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectCreateForm()

    return render(request, 'IMMP/dashboard.html', {'form': form})

def projects(request):
    return render(request,'IMMP/projects.html',{})

def adminDashboard(request):
    return render(request,'IMMP/admin-dashboard.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index2')
    else:
        form = UserCreationForm()
    return render(request,'IMMP/index2.html',{
        'form': form
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