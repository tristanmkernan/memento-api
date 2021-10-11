from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ("username", "is_staff", "is_superuser")



admin.site.register(User, MyUserAdmin)
