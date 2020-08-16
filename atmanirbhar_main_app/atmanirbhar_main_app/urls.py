"""atmanirbhar_main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    #generic view homepage
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    #generic view testpage -- login redirect
    path('test/', views.TestPage.as_view(), name="test"),
    #generic view thankspage -- logout redirect
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    #include user_accounts self made urls wih user_accounts/
    path('user_accounts/', include("user_accounts.urls", namespace="user_accounts")),
    #include user_accounts django builtin urls corresponding to django model wih user_accounts/
    path('user_accounts/', include("django.contrib.auth.urls")),
    #include user_accounts self made urls wih user_accounts/
    path('club_accounts/', include("club_accounts.urls", namespace="club_accounts")),
    path('events/', include("events.urls", namespace="events")),

    
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
