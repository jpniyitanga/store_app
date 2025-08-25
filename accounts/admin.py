from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Address, Customer


# Inline admin to manage addresses inside Customer
class AddressInline(admin.StackedInline):
    model = Address
    extra = 1
    verbose_name_plural = 'Addresses'


# Inline admin to manage Customer inside Account
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Customer Info'
    fk_name = 'user'
    autocomplete_fields = ['default_address']


# Make password read-only
@admin.register(Account)
class AccountAdmin(UserAdmin):
    model = Account
    inlines = [CustomerInline]
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


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ['user', 'phone_number', 'birth_date', 'default_address']
    search_fields = ['user__email', 'phone_number']
    autocomplete_fields = ['default_address']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'customer']
    search_fields = ['street', 'city', 'customer__user__email']
