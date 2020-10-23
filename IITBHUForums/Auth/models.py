from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()
    friends = models.ManyToManyField('self',blank=True,symmetrical=False)
    def __str__(self):
        return self.user.username
    def set_absolute_url(self):
        return '/profile/{}'.format(self.slug)

def create_profile(sender,**kwargs ):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile,sender=User)

class Relationship(models.Model):
    from_person = models.ForeignKey(Profile, related_name='from_people',on_delete=models.CASCADE)
    to_person = models.ForeignKey(Profile, related_name='to_people',on_delete=models.CASCADE)

class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="to_user",on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="from_user",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "From {},to {}".format(self.from_user.username,self.to_user.username)