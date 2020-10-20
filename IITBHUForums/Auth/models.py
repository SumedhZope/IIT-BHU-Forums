from django.db import models
from django.contrib.auth.models import User

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relationships = models.ManyToManyField('self', through='Relationship',
                                            symmetrical=False,
                                            related_name='related_to')
    def __str__(self):
        return self.user.username

class Relationship(models.Model):
    from_person = models.ForeignKey(user_profile, related_name='from_people',on_delete=models.CASCADE)
    to_person = models.ForeignKey(user_profile, related_name='to_people',on_delete=models.CASCADE)