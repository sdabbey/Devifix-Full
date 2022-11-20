from django.contrib import admin
from .models import UserPro, UserWork, User, Profile
# Register your models here.
admin.site.register(UserPro)
admin.site.register(UserWork)
admin.site.register(User)
admin.site.register(Profile)