from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
     path('', views.index ,name='index'),
    path('AboutHistory/', views.AboutHist ,name='AboutHistory'),
    path('AboutPrincipleMessage/', views.AboutPrincipleMessage ,name='AboutPrincipleMessage'),
    path('AboutVisionMission/', views.AboutVisionMission ,name='AboutVisionMission'),
   
    path('contact/', views.contact ,name='contact'),
    path('gallery/', views.gallery ,name='gallery'),
    path('more/', views.more ,name='more'),
    path('notices/', views.notices ,name='notices'),
    path('Notice_Open/<int:pk>', views.Notice_Open ,name='Notice_Open'),

    path('Admin/', views.Admin ,name='Admin'),
   
    path('logout/', views.logout_user ,name='logout'),
    

   
]
