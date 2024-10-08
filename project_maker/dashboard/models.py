from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_dashboard')


    def __str__(self):
        return f"{self.user.username}'s Dashboard"
    

class Widget(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='widgets')
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=240, blank=True, null=True)

    # Champs pour les information Back

    status = models.BooleanField(default=True)
    refresh_interval = models.PositiveIntegerField(default=60)  # Interval de raffrechissement du widget (en seconde)
    position = models.CharField(max_length=40, default="top-left")
    size = models.CharField(max_length=40, default="medium")
    color = models.CharField(max_length=40, default="beige")

    class Meta:
        abstract = True # Abstraite pour héritage
 