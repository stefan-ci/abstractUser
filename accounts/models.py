from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import now

def getExistingField(field_name):
    return AbstractUser._meta.get_field(field_name)

# Create your models here.
class CustomUser(AbstractUser):

    #Custom user fields
    #Add .is_custom to add to the form
    date_of_birth = models.DateTimeField(default=now())
    date_of_birth.fieldset = 'Important dates'
    date_of_birth.is_registration = True
    date_of_birth.is_custom = True
    date_of_birth.is_list_display = True
    nickname = models.CharField(max_length=50, null=True, blank=True)
    nickname.fieldset = 'New Category'
    nickname.is_custom = True
    nickname.is_registration = True
    nickname.is_list_filter = True

    #Use getExistingField(fieldname) to retrieve a field from AbstractUser model
    #You CAN use .is_registration, .is_list_filter and .is_list_display
    #You CANNOT use .is_custom
    email = getExistingField('email')
    email.is_registration = True
    email.is_list_filter = True

    pass

    def __str__(self):
        return self.username