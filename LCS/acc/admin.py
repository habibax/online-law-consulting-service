from django.contrib import admin

from acc.models import AdminProfile, User, UserProfile, LawyerProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(AdminProfile)
admin.site.register(LawyerProfile)