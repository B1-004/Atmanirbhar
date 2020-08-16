from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# pip install misaka
import misaka

from club_accounts.models import Club_User
#from user_accounts.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

#choices for specifying event creator type
event_creator_type_choices =(
    ("user","Created by Student"),
    ("club_user","Created by Club")
)

#choices when user subscribes for an event
event_category_choices_prior = (
    ("red", "Will be Going"),
    ("yellow", "Intrested"),
    ("green", "Not Going")
)

#choices when an event starts
event_category_choices_posterior = (
    ("white", "Attended"),
    ("black", "Did not Attend"),
    ("grey", "I Do not Know")
)


class Event(models.Model):
    
    event_name = models.CharField(max_length=255, unique=False)
    created_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()    
    event_coordinator = models.ForeignKey(User, related_name="event_coordi", on_delete=models.CASCADE)
    description = models.TextField()
    description_html = models.TextField(editable=False)

    #slug = models.SlugField(allow_unicode=True, unique=True) #used for making custom url with event name

    #event_creator_type = models.CharField(editable=False, choices=event_creator_type_choices)
    #event_club = models.ForeignKey(Club_User, editable= False, related_name="event_by_club", on_delete=models.CASCADE, null=True, blank=True)
    
    #event_subcription_category = models.CharField(editable=False, choices=event_category_choices_prior, blank=True)
    #subscribed_event_attendance = models.CharField(editable=False, choices=event_category_choices_posterior, blank=True)

    #subscribers = models.ManyToManyField(User,through="Event_Subscriber")


    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.event_name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "events:single", #detailed view of the event when opened by user to check details or subcribe
            kwargs={
                #"username": self.event_coordinator.username, #event_coordi username
                "pk": self.pk #primary key of event
            }
        )

    def is_past(self):
        if timezone.now() > self.end_time:
            return True
        return False



    class Meta:
        ordering = ["-created_at"]
        unique_together = ["event_name", "event_coordinator"]
        #below code to be used if working with "event_club" also as a relation
        #constraints = [
        #    UniqueConstraint(fields=["event_name", "event_coordinator", "event_club"],
        #                     name='unique_with_club_event'),
        #    UniqueConstraint(fields=["event_name", "event_coordinator"],
        #                     condition=Q(optional=None),
        #                     name='unique_without_club_event'),
        #]





"""
class Event_Subscriber(models.Model):
    #created event_name to link to users --refrencing will be this when accesing Event_Member: event_name belong to Event table  
    event_name = models.ForeignKey(Event,related_name='event_subcriptions',on_delete=models.CASCADE) 
    
    #created users to link to event_name --refrencing will be this when accesing Event_Member: users belong User table  
    users = models.ForeignKey(User,related_name='user_subscribed_events',on_delete=models.CASCADE)

    def __str__(self):
        return self.users.username

    class Meta:
        unique_together = ("event_name", "users") #set the link
"""