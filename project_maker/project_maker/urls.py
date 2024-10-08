"""
URL configuration for project_maker project.

"""

from django.contrib import admin
from django.urls import path, include

from authentication.views import LoginPageView, logout_user
from dashboard.views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout_user, name='logout'),
    path('', LoginPageView.as_view(), name='login'),
    path('home/', homeView,  name='home')
]
