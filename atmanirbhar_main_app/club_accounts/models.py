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


# Create your models here.
class Club_User(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    coordinatorid =models.ForeignKey(User, related_name='is_coordinator', on_delete= models.CASCADE, unique=False, default='none')
    fa_name = models.CharField(max_length=30, unique=False, default='none')

    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=False, default='Our Club rocks!')#"Welcome to: "+Club_User.name+"Greeting From Coordinator: "+Club_User.coordinatorid+"And FA: "+Club_User.fa_name) 
    description_html = models.TextField(editable=False, default='', blank=True)
    
    members = models.ManyToManyField(User,through="Club_Member")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("club_accounts:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


class Club_Member(models.Model):
    club_name = models.ForeignKey(Club_User,related_name='club_memberships',on_delete=models.CASCADE)
    users = models.ForeignKey(User,related_name='user_clubs',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("club_name", "users")
