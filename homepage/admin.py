from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
 
from .models import Profile
 
class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = '추가정보'
 
class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)  
admin.site.register(User, ProfileAdmin)