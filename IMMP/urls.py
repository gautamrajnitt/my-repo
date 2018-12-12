from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('projects.html', views.projects, name='projects'),
    path('members.html', views.members, name='members'),
    path('team.html', views.team, name='team'),
    path('contact.html', views.contact, name='contact'),
    path('faq.html', views.faq, name='faq'),
    path('signup.html', views.signup, name='signup'),
    path('login.html', views.login, name='login'),
]