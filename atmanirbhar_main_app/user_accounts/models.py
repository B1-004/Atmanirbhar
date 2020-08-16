from django.db import models
from django.contrib import auth
from django.utils import timezone

from events.models import Event
# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    #P.S. : used builtin django login system for future versions need to create user model

    def __str__(self):
        return "@{}".format(self.username)

