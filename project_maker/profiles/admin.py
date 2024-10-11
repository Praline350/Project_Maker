from django.contrib import admin
from .models import Profile, Color, Palette, UiSetting


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ["user", "text_color"]


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    list_display = ["name", "hex_code"]


@admin.register(Palette)
class AdminPalette(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(UiSetting)
class AdminUiSetting(admin.ModelAdmin):
    list_display = ["profile", "background_color"]
