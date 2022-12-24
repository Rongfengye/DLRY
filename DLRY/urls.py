from django.contrib import admin
from django.urls import path, include

from DLRY import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('dylan_page', views.dylan_page, name='dylan'),
    path('rong_page', views.rong_page, name='rong'),
    path('side_quests', views.side_quests, name='sidequests'),
]