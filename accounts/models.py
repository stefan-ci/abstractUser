from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateTimeField(default=now())
    date_of_birth.fieldset = 'Personal info'
    date_of_birth.is_custom = True
    pet_name = models.CharField(max_length=50, null=True, blank=True)
    pet_name.fieldset = 'Personal info'
    pet_name.is_custom = True

    pass

    def __str__(self):
        return self.username