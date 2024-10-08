from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


    def clean_age(self):
        if self.age < 15:
            raise ValidationError('Age requis : 15ans minimum')