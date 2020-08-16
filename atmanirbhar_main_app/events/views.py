from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Event
from . import models

class CreateEvent(LoginRequiredMixin, generic.CreateView):
    fields =( "event_name","description", "start_time", "end_time", "event_coordinator")
    model = Event


#generic view made
class SingleEvent(generic.DetailView):
    model = Event

#generic view made
class ListEvents(generic.ListView):
    model = Event

