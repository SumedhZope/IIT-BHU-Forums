from django.db import models

# Create your models here.
class group(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    #group_icon=models.ImageField()
    #group_id=models.IntegerField(default=0)
