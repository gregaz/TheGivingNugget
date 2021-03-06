from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	balance = models.IntegerField( default = 0)
	linkedAccount = models.TextField( default = '')

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)