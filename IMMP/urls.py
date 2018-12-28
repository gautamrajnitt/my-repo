from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('projects', views.projects, name='projects'),
    # path('members', views.members, name='members'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    # path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('newproject', views.newproject, name='newproject'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('index2', views.index2, name='index2'),
    path('admin-dashboard/', views.adminDashboard, name='index2'),
    # path('signup/', views.SignUpView.as_view(), name='signup')
]