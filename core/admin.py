from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, OrganizationProfile

# Inline admin classes for profiles


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class OrganizationProfileInline(admin.StackedInline):
    model = OrganizationProfile
    can_delete = False

# Customizing the User admin


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, OrganizationProfileInline)


# Unregister the default User admin and register the custom User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register other models with admin
admin.site.register(Profile)
admin.site.register(OrganizationProfile)
