from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField(default="Most sensibel talks")
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.DateField(auto_now_add=True)
    created_by = models.TextField(default=' ')
    group =  models.ForeignKey(Group,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title
