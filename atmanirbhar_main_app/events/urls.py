from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.ListEvents.as_view(), name="all"),
    path("new/", views.CreateEvent.as_view(), name="create"),
    path("events/in/<pk>/",views.SingleEvent.as_view(),name="single"),
]
