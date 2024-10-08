from django.contrib import admin
from .models import Dashboard, Widget


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ['user', ]

