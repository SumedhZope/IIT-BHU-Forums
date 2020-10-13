from django.db import models
from django.contrib.auth.models import User
import datetime

class Group(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField(default="Most sensibel talks")
    created_at = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
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
