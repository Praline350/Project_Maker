from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()  # Appel à la méthode clean de la classe parente
        self.clean_age()  # Appel à votre méthode de validation personnalisée

    def clean_age(self):
        if (
            self.age is not None and self.age < 15
        ):  # Vérification de l'existence de l'âge
            raise ValidationError("Age requis : 15 ans minimum")
