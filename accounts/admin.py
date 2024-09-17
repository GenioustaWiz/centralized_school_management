from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Select User Type', {'fields': ('user_type')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', 'phone_number', 'image')}),
        # ('Social Media', {'fields': ('github', 'facebook', 'googleplus', 'instagram')}),
        ('Permissions', {'fields': ('user_type','is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        # ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )
    #Change the ordering from Username to Email coz their's no Username in the models
    ordering = ('email',) 
admin.site.register(User, CustomUserAdmin)