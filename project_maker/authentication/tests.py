import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client

from .views import LoginPageView


@pytest.mark.django_db
class TestLoginPageView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.signup_url = reverse(
            "login"
        )  # Remplace 'login' par le nom de ton URL pour la vue
        self.UserModel = get_user_model()

    def test_get_login_page(self):
        response = self.client.get(self.signup_url)
        assert response.status_code == 200
        assert response.templates[0].name == LoginPageView.template_name

    def test_login_with_valid_credentials(self):
        # Créer un utilisateur
        self.UserModel.objects.create_user(
            username="testuser", password="password123"
        )
        assert self.UserModel.objects.filter(username="testuser").exists()
        # Essayer de se connecter
        login_data = {
            "login_username": "testuser",
            "password": "password123",
            "login_form": "",
        }
        response = self.client.post(self.signup_url, login_data)
        assert response.status_code == 302  # Redirection après connexion

    def test_signup_creates_new_user(self):
        signup_data = {
            "email": "email@email.com",
            "username": "newuser",
            "password1": "password123123",
            "password2": "password123123",
            "signup_form": "",
        }
        response = self.client.post(self.signup_url, signup_data)
        assert response.status_code == 302  # Redirection après inscription
        assert self.UserModel.objects.filter(username="newuser").exists()
