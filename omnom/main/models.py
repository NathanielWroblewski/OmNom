from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PickupRequest(models.Model):
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    requester = models.ForeignKey(User,related_name="requests")

    is_fulfilled = models.BooleanField(default=False)
    fulfilled_by = models.ForeignKey(User,related_name="fulfilled_requests",null=True,blank=True)
    is_picked_up = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    expiry = models.IntegerField(default=24) # number of hours since created

class Feedback(models.Model):
    pickup_request = models.ForeignKey(PickupRequest)
    from_user = models.ForeignKey(User,related_name="feedbacks_given")
    to_user = models.ForeignKey(User,related_name="feedbacks_received")

    rating = models.IntegerField()
    feedback = models.TextField()

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    phone_number = models.CharField(max_length=127,null=True,blank=True)
    donater_description = models.TextField(null=True, blank=True) #not required

    @property
    def reputation(self):
        return 5


from main.receivers import *
