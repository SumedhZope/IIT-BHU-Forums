from django.db import models

# Create your models here.
class UserProfile(models.Model):
    UserName = models.CharField(max_length=140)  
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)
    Bio = models.CharField(max_length=1000)  

