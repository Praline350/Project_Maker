from django.conf import settings

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

from django.views.generic import View
from django.contrib import messages

from .forms import LoginForm, SignupForm

User = get_user_model()


class LoginPageView(View):
    template_name = "authentication/login.html"
    login_form_class = LoginForm
    signup_form_class = SignupForm

    def get(self, request):
        """Handle GET requests: instantiate blank forms for login and sign up."""

        if request.user.is_authenticated:
            return redirect('home')
        login_form = self.login_form_class()
        signup_form = self.signup_form_class()
        context = {
            "login_form": login_form,
            "signup_form": signup_form
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        """Handle POST requests: authenticate user or create a new account."""
        login_form = self.login_form_class(request.POST)
        signup_form = self.signup_form_class(request.POST)
        print("Login form data:", request.POST)
        if 'login_form' in request.POST:
            if login_form.is_valid():
                print("Login form is valid.")
                print("Trying to authenticate with username:", login_form.cleaned_data["login_username"], "and password:", login_form.cleaned_data["password"])

                user = authenticate(
                    username=login_form.cleaned_data["login_username"],
                    password=login_form.cleaned_data["password"],
                )
                print("Authenticated user:", user)
                if user is not None:
                    login(request, user)
                    print("User logged in:", request.user)
                    return redirect('home')
                else:
                    messages.error(request, "Identifiants Invalides")
                    print(login_form.errors)
        if "signup_form" in request.POST:
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Erreur d'inscription")
                print(signup_form.errors)
        context = {
            "login_form": login_form,
            "signup_form": signup_form,
        }
        return render(request, self.template_name, context=context)
    
@login_required
def logout_user(request):
    """Log out the user and redirect to the login page."""
    logout(request)
    return redirect("login")