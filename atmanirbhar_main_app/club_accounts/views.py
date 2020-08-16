from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Club_User,Club_Member
from . import models

#generic view made
class SingleClub(generic.DetailView):
    model = Club_User

#generic view made
class ListClubs(generic.ListView):
    model = Club_User

#generic view made
class JoinClub(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs): #redirect to that club page after joining
        return reverse("club_accounts:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs): #create user member of that club
        club = get_object_or_404(Club_User,slug=self.kwargs.get("slug"))

        try:
            Club_Member.objects.create(users=self.request.user,club_name=club)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(club.name)))

        else:
            messages.success(self.request,"You are now a member of the {} club.".format(club.name))

        return super().get(request, *args, **kwargs)


#generic view made
class LeaveClub(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs): #redirect to that club page after leaving
        return reverse("club_accounts:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs): #delete user as member of that club
        try:
            club_memberships = models.Club_Member.objects.filter(
                users=self.request.user,
                club_name__slug=self.kwargs.get("slug")
            ).get()

        except models.CLub_Member.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this club because you aren't in it."
            )

        else:
            club_memberships.delete()
            messages.success(
                self.request,
                "You have successfully left this club."
            )
        return super().get(request, *args, **kwargs)
