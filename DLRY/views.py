
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone
from DLRY.models import SideQuest
from DLRY.forms import SideQuestForm
# Create your views here.


def home_page(request):
    context = dict()
    return render(request, 'DLRY/home_page.html', context)

def dylan_page(request):
    context = dict()
    context['name'] = "Dylan Lai"
    context['paragraph_1'] = "Im cool"
    context['paragraph_2'] = "Im very cool"

    return render(request, 'DLRY/dylan_page.html', context)

def rong_page(request):
    context = dict()
    context['name'] = "Rong Ye"
    context['paragraph_1'] = "Im cool"
    context['paragraph_2'] = "Im very cool"
    return render(request, 'DLRY/rong_page.html', context)

def side_quests(request):
    context = dict()

    
    # context['quests'] = SideQuest.objects.all()

    if request.method == "GET":
        context['form'] = SideQuestForm()

    else:
        new_form = SideQuestForm(request.POST, request.FILES)
    

        print(f'the submitted form {new_form}')

        # Validates the form.
        if not new_form.is_valid():
            return render(request, 'DLRY/side_quests.html', context)

        new_sidequest = SideQuest(title=new_form.cleaned_data['title'],description=new_form.cleaned_data['description'], video=new_form.cleaned_data['video'])
        new_sidequest.save()

        allSubmitted = SideQuest.objects.all()
        print(f'these are all the submitted videos {allSubmitted}')

        context['form'] = SideQuestForm()

        # return render(request, 'DLRY/side_quests.html', context)

    # Else we are here as a result of a submit
    questList = []
    count = 0
    for item in SideQuest.objects.all():
        if (count % 2 == 0):
            questList.append([item])
        else: 
            questList[-1].append(item)
        count += 1

    context['quests'] = questList
    
    return render(request, 'DLRY/side_quests.html', context)
