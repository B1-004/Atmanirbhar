from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse

import misaka

# from user_accounts.models import User #incase customized user model
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


# Create your models here.
class Club_User(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    coordinatorid =models.ForeignKey(User, related_name='is_coordinator', on_delete= models.CASCADE, unique=False) #coordi roll number
    fa_name = models.CharField(max_length=30, unique=False)

    slug = models.SlugField(allow_unicode=True, unique=True) #used for making custom url with club name
    description = models.TextField(blank=False, default='Our Club rocks!') 
    description_html = models.TextField(editable=False, default='', blank=True)
    
    members = models.ManyToManyField(User,through="Club_Member")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("club_accounts:single", kwargs={"slug": self.slug}) #takes to club detail page

    class Meta:
        ordering = ["name"]



class Club_Member(models.Model):
    #created club_name to link to users --refrencing will be this when accesing Club_Members: club_name belong to Club_User table  
    club_name = models.ForeignKey(Club_User,related_name='club_memberships',on_delete=models.CASCADE) 
    
    #created users to link to club_name --refrencing will be this when accesing Club_Members: users belong User table  
    users = models.ForeignKey(User,related_name='user_clubs',on_delete=models.CASCADE)

    def __str__(self):
        return self.users.username

    class Meta:
        unique_together = ("club_name", "users") #set the link
