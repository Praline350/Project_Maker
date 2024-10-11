from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_dashboard")
    background_color = models.CharField(max_length=40, default="white")
    background_image = models.ImageField(upload_to="background_images/", blank=True, null=True)
    # theme = models.CharField(max_length=128, blank=True, null=True) # Theme deja prè établi
    # TODO : Ajouté plutot une relation a une table theme

    def __str__(self):
        return f"{self.user.username}'s Dashboard"


class Widget(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="widgets")
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    # Champs pour les informations Back-end

    status = models.BooleanField(default=True)
    refresh_interval = models.PositiveIntegerField(default=60)  # Interval de raffraichissement du widget (en seconde)

    # Champs pour le Front-end

    # theme = models.CharField(max_length=128, blank=True, null=True)  # Theme deja prè établi
    icon = models.ImageField(upload_to="widgets_icons/", blank=True, null=True)
    position = models.CharField(max_length=40, blank=True, null=True)  # ID de la cellule de la grille du dashboard

    resizable = models.BooleanField(default=True)
    size = models.CharField(max_length=40, default="medium")
    min_height = models.IntegerField(default=100)
    max_height = models.IntegerField(default=600)
    min_width = models.IntegerField(default=100)
    max_width = models.IntegerField(default=400)

    color = models.CharField(max_length=40, default="beige")
    border_color = models.CharField(max_length=40, default="black")

    class Meta:
        abstract = True  # Abstraite pour héritage
