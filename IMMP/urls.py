from django.urls import path
from . import views
from app import views as appviews

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('members', views.members, name='members'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('newproject', views.newproject, name='newproject'),
    path('dashboard/', appviews.index, name='dashboard'),
]