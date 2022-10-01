from django.contrib import admin

from acc.models import AdminProfile, User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(AdminProfile)