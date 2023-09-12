from user_profile.models import Profile

from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
