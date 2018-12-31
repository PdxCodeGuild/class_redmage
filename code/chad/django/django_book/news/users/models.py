from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)