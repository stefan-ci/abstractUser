from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'pet_name',]
    list_filter = ['email', 'username', 'date_of_birth', 'pet_name',]

    # This setting is used to select the fields displayed on the change/registration form
    fieldsets = (
        ('Personal Details', {'fields': ('username', 'email', 'password', 'date_of_birth', 'pet_name',)}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',
                       'date_of_birth', 'pet_name')}
         ),
    )

admin.site.register(CustomUser, CustomUserAdmin)