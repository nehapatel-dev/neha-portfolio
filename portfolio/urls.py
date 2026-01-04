from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('skills/',views.skills,name='skills'),
    path('project/',views.project,name='project'),
    path('education/',views.education,name='education'),
    path('contact/',views.contact,name='contact'),




]



