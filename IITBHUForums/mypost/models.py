from django.db import models

# Create your models here.
class mypost(models.Model):
    post_pic=models.ImageField(upload_to='thumbpath',blank=True)
    caption= models.CharField(max_length=20000)