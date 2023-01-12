from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home),
    path('home/',views.home),
    path('index/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('services/',views.services),
    path('viewnews/',views.vnews),
    path('videos/',views.videogallery),
    path('login/',views.login),
    path('viewmore/',views.viewmore),
    path('vnews/',views.vnews),
]
