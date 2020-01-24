from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateTimeField(default=now())
    pet_name = models.CharField(max_length=50, null=True, blank=True)
    pass

    def __str__(self):
        return self.username