from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources
    # Or create a separate django app.
    #path('', views.gentella_html, name='gentella'),

    # The home page
    path('projects/all/', views.media_gallery, name='media_gallery'),
    path('projects/liked/', views.liked_projects, name='liked_projects'),
    path('details/<int:product_id>/', views.details, name='details'),
    path('projects/upload/', views.upload_project, name='upload_project'),
    path('skills/', views.skills, name='skills'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)