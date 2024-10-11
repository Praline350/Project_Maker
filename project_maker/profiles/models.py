from django.db import models
from django.contrib.auth import get_user_model

from PIL import Image

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatar_profiles", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}' Profile"


class Color(models.Model):
    name = models.CharField(max_length=48)
    hex_code = models.CharField(max_length=7)  # exemple: '#FFFFFF'

    def __str__(self):
        return f"{self.name} ({self.hex_code})"


class Palette(models.Model):
    name = models.CharField(max_length=128)
    primary = models.ForeignKey(Color, related_name="primary_palette", on_delete=models.CASCADE)
    secondary = models.ForeignKey(Color, related_name="secondary_palette", on_delete=models.CASCADE)
    background = models.ForeignKey(Color, related_name="background_palette", on_delete=models.CASCADE)
    text_color = models.ForeignKey(Color, related_name="text_color_palette", on_delete=models.CASCADE)

    def __str__(self):
        return f"Palette {self.name}"


class UiSetting(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="profile_uisetting")
    background_color = models.CharField(max_length=40, default="")
    palette = models.ForeignKey(Palette, on_delete=models.SET_NULL, null=True, blank=True)
