from django.urls import path
from . import views

app_name = 'club_accounts'

urlpatterns = [
    path('', views.ListClubs.as_view(), name="all"),
    path("club/in/<slug>/",views.SingleClub.as_view(),name="single"),
    path("join/<slug>/",views.JoinClub.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveClub.as_view(),name="leave"),
]
