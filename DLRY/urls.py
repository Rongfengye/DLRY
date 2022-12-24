from django.contrib import admin
from django.urls import path, include

from DLRY import views

urlpatterns = [
    path('', views.home_page, name='home')
]