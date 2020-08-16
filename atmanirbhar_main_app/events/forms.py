from django import forms
from . import models

class EventCreationForm(forms.ModelForm):
    class Meta:
        fields =( "event_name","description", "start_time", "end_time", "event_coordinator")
        model = models.Post

    def __init__(self, *args, **kwargs):
        event_coordinator = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        #if event_coordinator is not None:

