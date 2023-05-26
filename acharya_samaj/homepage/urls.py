from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('home/', views.home, name="home"),
    path('notice/', views.notice, name="notice"),
    path('about/', views.about, name="about"),
]

