from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    """Admin class for ``User`` model."""

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'email',
                'first_name',
                'last_name',
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Dates', {
            'fields': (
                'last_login',
                'date_joined',
            ),
        }),
    )
    list_display = (
        'username',
        'email',
        'is_staff',
        'is_superuser',
    )
