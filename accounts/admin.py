from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Make password read-only
@admin.register(Account)
class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    list_display_links = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = (['-date_joined'])
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = ((None, {
        'fields': (
            'email', 'username', 'password'
        )
    }),
        ('Personal Info', {
            'fields': (
                'first_name', 'last_name', 'phone_number', 'birth_date'
            )
        }),
        ('Address', {
            'fields': (
                'street', 'city', 'province', 'postal_code', 'country'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name',
                'password1', 'password2', 'phone_number', 'birth_date',  'street', 'city', 'province', 'postal_code', 'country',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )
