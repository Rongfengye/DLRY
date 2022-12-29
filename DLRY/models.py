from django.db import models
from django.contrib.auth.models import User

class SideQuest(models.Model):
    # creator = models.ForeignKey(User, on_delete=models.PROTECT) # Either DL, RY
    title = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=200)
    # video = models.FileField(upload_to='static/DLRY/videos')
    # video = models.FileField(upload_to='static/DLRY/videos')
    # video = models.FileField(upload_to='DLRY/static/DLRY/videos')
    video = models.FileField(upload_to='videos/', null=True, verbose_name="")

    # prob should use static url
    def __str__(self):
        return self.title + "," + self.description + " : "+ str(self.video)


class ProfilePic(models.Model):

    image = models.FileField(upload_to='images/')