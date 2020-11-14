from django.db import models
from django.contrib.auth.models import User
from Auth.models import Profile
from django.urls import reverse
import datetime
from PIL import Image


class Group(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField(default="Most sensibel talks")
    groupicon = models.ImageField(upload_to ="groupicon/",default = 'screenshot_4.png')
    created_at = models.DateTimeField()
    likes = models.IntegerField()
    liked_by = models.ManyToManyField(User,related_name='people_liked')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    members = models.ManyToManyField(Profile, blank=True)
    def __str__(self):
        return self.name
      
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=' ')
    created_at = models.DateTimeField(default=datetime.datetime.now())
    group =  models.ForeignKey(Group,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_abs_url(self):
        return reverse('post_view',kwargs={
            'id' : self.id
        })

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    created_at = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

class like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return "by {} on {}".format(self.user,self.post)

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.role} to {self.user.username} in {self.group.name}"

class Role_choices(models.Model) : 
    group = group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.role} in {self.group.name}"