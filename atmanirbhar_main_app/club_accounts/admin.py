from django.contrib import admin
from . import models

# Register your models here.
class Club_MemberInline(admin.TabularInline):
    model = models.Club_Member

admin.site.register(models.Club_User)
