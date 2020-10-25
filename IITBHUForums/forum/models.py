from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image


class Group(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField(default="Most sensibel talks")
    groupicon = models.ImageField(upload_to ="groupicon/")
    created_at = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   # admin = models.OneToOneField(User,on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        baseheight = 560
        img = Image.open(self.groupicon.path)
        print(img.width)
        print(img.height)
        croped = img.crop((0,0,int(img.height*1.75),img.height))
        croped.save(self.groupicon.path,quality = 90)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=' ')
    created_at = models.DateField(default=datetime.datetime.now())
    group =  models.ForeignKey(Group,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
