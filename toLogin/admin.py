from django.contrib import admin

from toLogin.models import CustomUser, UserProfile

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserProfile)




