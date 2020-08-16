from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_accounts'

urlpatterns = [
    #generic view used but attached a template for better formating
    path('login/', auth_views.LoginView.as_view(template_name="user_accounts/login.html"),name='login'),
    #generic view used but attached a template for better formating
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
    #generic view used but attached a template for better formating
    path('signup/', views.SignUp.as_view(template_name="user_accounts/signup.html"), name="signup"),
]
