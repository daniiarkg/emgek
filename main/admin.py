from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin
from django.contrib.auth.models import User

from main.models import E_user

admin.site.register(E_user, UserAdmin)
