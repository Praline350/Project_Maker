import pytest
from django.contrib.auth import get_user_model
from dashboard.models import Dashboard, Widget

User = get_user_model()

@pytest.mark.django_db  # Cette annotation permet d'accéder à la base de données
class TestDashboard:

    def test_dashboard_creation(self):
        user = User.objects.create(username='testuser')
        dashboard = Dashboard.objects.create(user=user, background_color='blue')
        
        assert dashboard.user == user
        assert dashboard.background_color == 'blue'
        assert str(dashboard) == "testuser's Dashboard"

@pytest.mark.django_db
class TestWidget:

    def test_widget_creation(self):
        user = User.objects.create(username='testuser')
        dashboard = Dashboard.objects.create(user=user, background_color='blue')
        
        widget = Widget.objects.create(dashboard=dashboard, name='Test Widget', description='A test widget', status=True)

        assert widget.dashboard == dashboard
        assert widget.name == 'Test Widget'
        assert widget.description == 'A test widget'
        assert widget.status is True