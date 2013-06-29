from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from main.models import UserProfile

@receiver(post_save, 
          sender=User,
          dispatch_uid="create_user_profile")
def create_user_profile(sender,instance, **kwargs):
    if kwargs['created']:
        UserProfile(user=instance).save()
