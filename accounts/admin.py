from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    date_hierarchy = 'date_joined'
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    custom_fields = {}
    new_fields = ()

    for field in CustomUser._meta.get_fields():
        if field.__dict__.get('is_custom') == True:
            fset = field.__dict__.get('fieldset')
            if fset in custom_fields:
                custom_fields[fset].append(field.__dict__.get('name'))
            else:
                custom_fields[fset] = [field.__dict__.get('name')]
    #print(custom_fields)
    new_fields = []

    for fieldset in list(UserAdmin.fieldsets):
        if fieldset[0] != None and fieldset[0] in custom_fields:
            new_fields.append((fieldset[0],
                               {'fields': tuple(list(fieldset[1]['fields']) + list(custom_fields[fieldset[0]]))
                               }))
        else:
            new_fields.append(fieldset)
    print(tuple(new_fields))
        #new_fields = new_fields + (fieldset[1][0], fieldset[1][1]['fields'].append(custom_fields[fieldset[0]]))
    

    
    #fieldsets = UserAdmin.fieldsets
    fieldsets = tuple(new_fields)
    #print(fieldsets[1][1]['fields'])

    
    list_display = ['email', 'username', 'date_of_birth', 'pet_name',]
    list_filter = ['email', 'username', 'date_of_birth', 'pet_name',]

    # This setting is used to select the fields displayed on the change/registration form
    #fieldsets = (
    #    ('Personal Details', {'fields': ('username', 'email', 'password', 'date_of_birth', 'pet_name',)}),

    #)

    #fieldsets = CustomUser._meta.get_fields()

    # TODO: remove; just for testing
    print("FIELDS")
    current_fields = ()
    for field in CustomUser._meta.get_fields():
        field.get_internal_type()
        for key, value in field.__dict__.items():
            if key == 'name' and value != 'id':
                current_fields = current_fields + (value, )
        #current_fields = current_fields + (field.__dict__['name'], )
    print(current_fields)

    fieldsets = (
        (None, {'fields': current_fields}),
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