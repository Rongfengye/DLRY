from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from DLRY.models import SideQuest, ProfilePic

class SideQuestForm(forms.ModelForm):
    class Meta:
        model = SideQuest
        fields = ('title','description', 'video')
        widgets = {
            'title': forms.Textarea(attrs={'id':'id_quest_input_title', 'rows':'1'}),
            'description': forms.Textarea(attrs={'id':'id_quest_input_description', 'rows':'3'}),
            'video': forms.FileInput(attrs={'id':'id_profile_video'})
        }
        labels = {
            'title': 'SideQuest',
            'description': 'Enter Description',
            'video': 'Upload Video',
        }

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = {'image'}
        widgets = {
            'image': forms.FileInput(attrs={'id':'id_profile_picture'})
        }
        labels = {
            'image': 'Upload Image',
        }