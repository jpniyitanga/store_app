from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Make password read-only
class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'last_login', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    # Make first_name and last_name clickable
    list_display_links = ('email', 'first_name', 'last_name')

    readonly_fields = ('last_login', 'date_joined')
    ordering = (['-date_joined'])
    filter_horizontal = ('groups', 'user_permissions')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name',
                'password1', 'password2',
                'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
