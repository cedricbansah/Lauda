from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from lauda.models import User, Driver


class ManagerAdmin(UserAdmin):
    list_display = (
        'id', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'last_login', 'date_joined')
    search_fields = ('id', 'email', 'first_name', 'last_name',)

    ordering = ('id',)

    fieldsets = (
        ('Admin Information', {
            'fields': (
                'email', 'password', 'first_name', 'last_name', 'contact', 'is_active',
                'is_superuser', 'groups', 'user_permissions',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'contact', 'is_superuser', 'groups',
                'user_permissions'),
        }),
    )

    def get_changelist_instance(self, request):
        changelist_instance = super().get_changelist_instance(request)
        if changelist_instance:
            changelist_instance.title = _('Managers')
        return changelist_instance

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filter the queryset to show only records with user_type 'admin'
        return qs.filter(driver__isnull=True)

    def save_model(self, request, obj, form, change):
        if not change:  # Checking if it's a new record
            obj.is_staff = True

        super().save_model(request, obj, form, change)



class DriverAdmin(UserAdmin):
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'last_login',
        'date_joined',
        'date_of_birth',
        'phone_number',
        'license_number',
        'address',
        'vehicle_assigned'
    )
    search_fields = ('id', 'email', 'first_name', 'last_name',)

    ordering = ('id',)

    fieldsets = (
        ('Driver Information', {
            'fields': (
                'email',
                'password',
                'first_name',
                'last_name',
                'phone_number',
                'is_active',
                'address',
                'license_number',
                'date_of_birth'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'address',
                'license_number', 'date_of_birth'),
        }),
    )

    def get_changelist_instance(self, request):
        changelist_instance = super().get_changelist_instance(request)
        if changelist_instance:
            changelist_instance.title = _('Drivers')
        return changelist_instance



# Register your models here.
admin.site.register(User, ManagerAdmin)
admin.site.register(Driver, DriverAdmin)
