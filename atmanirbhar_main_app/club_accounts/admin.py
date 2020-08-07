from django.contrib import admin
from . import models

# Register your models here.
class Club_MemberInline(admin.TabularInline): #done to make club_member inline with club_user check internet for details
    model = models.Club_Member

admin.site.register(models.Club_User)
