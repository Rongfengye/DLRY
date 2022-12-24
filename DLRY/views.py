
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone
# Create your views here.


def home_page(request):
    context = dict()
    return render(request, 'DLRY/home_page.html', context)

def dylan_page(request):
    context = dict()
    return render(request, 'DLRY/dylan_page.html', context)

def rong_page(request):
    context = dict()
    return render(request, 'DLRY/rong_page.html', context)

def side_quests(request):
    context = dict()
    return render(request, 'DLRY/side_quests.html', context)

