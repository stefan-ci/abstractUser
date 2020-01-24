# Django Abstract User

This project is meant to demonstrate how to create a custom Django user model

Steps:
1. Create new app (e.g. accounts)
2. Create new CustomUser model
3. Update `settings.py`
4. Create new `UserCreation` and `UserChangeForm`
5. Update `admin.py`

## 1. Create new app
Create a new Django app that will handle all of the custom user logic.
Type in the terminal:

`django-admin startapp accounts`

## 1. Create new CustomUser model
In the accounts/models.py add your CustomUser model which should inherit <br />
from AbstracUser. You can add some extra fields now (e.g DOB, pet name, etc.). <br />
See an example of the new CustomUser model below.

```
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
```

Make changes in the database

```
python manage.py makemigrations
python manage.py migrations
```

## 3. Update `settings.py`
Add the new app to your INSTALLED_APPS list in `settings.py`

```
...
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # new app handling custom user logic
    'accounts',
]

# associate our new CustomUser model
AUTH_USER_MODEL = 'accounts.CustomUser' 

...
```

## 4. Create new `UserCreation` and `UserChangeForm`

Create a new `forms.py` file in the accounts directory.
In the `forms.py`
