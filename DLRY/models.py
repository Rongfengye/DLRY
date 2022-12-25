from django.db import models
from django.contrib.auth.models import User

class SideQuest(models.Model):
    # creator = models.ForeignKey(User, on_delete=models.PROTECT) # Either DL, RY
    title = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=200)
    video = models.FileField(upload_to='uploads/')
    