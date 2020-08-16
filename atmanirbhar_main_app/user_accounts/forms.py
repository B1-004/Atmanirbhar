from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    #P.S. : used builtin django login system for future versions need to create user model and subsequent form and validators
    class Meta:
        fields = ("username","first_name", "last_name","email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Institute roll number" #django.contrib.auth User Builtin username field is used as primarykey taken as roll number here 
        self.fields["email"].label = "Institute Email address" #create new model for additional emails
