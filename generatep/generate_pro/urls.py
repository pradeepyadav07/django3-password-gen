
from django.contrib import admin
from django.urls import path
from generator import views
urlpatterns = [
    path('', views.home),
    path('genpassword/', views.password, name='password'),
]
