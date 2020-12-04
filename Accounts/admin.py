from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ProgramStudi, User, Account
# Register your models here.

@admin.register(User)
class UserModelAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields' : ('email', 'username', 'password')}),
        ('Personal Detail', {'fields' : ('first_name', 'last_name', 'prodi', 'roles','profile_picture')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields' : ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('username', 'email', 'password1', 'password2', 'prodi', 'roles')}
        ),
    )

admin.site.register(ProgramStudi)
admin.site.register(Account)
