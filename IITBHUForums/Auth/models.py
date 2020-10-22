from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friend = models.ManyToManyField('self',blank=True,symmetrical=False)
    def __str__(self):
        return self.user.username

class Relationship(models.Model):
    from_person = models.ForeignKey(userprofile, related_name='from_people',on_delete=models.CASCADE)
    to_person = models.ForeignKey(userprofile, related_name='to_people',on_delete=models.CASCADE)