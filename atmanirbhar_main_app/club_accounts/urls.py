from django.urls import path
from . import views

app_name = 'club_accounts'

urlpatterns = [
    #generic view - All Club list view
    path('', views.ListClubs.as_view(), name="all"),
    #generic view - Single Club detailed view
    path("club/in/<slug>/",views.SingleClub.as_view(),name="single"),
    #generic view - Join Club view
    path("join/<slug>/",views.JoinClub.as_view(),name="join"),
    #generic view - Leave Club view
    path("leave/<slug>/",views.LeaveClub.as_view(),name="leave"),
]
