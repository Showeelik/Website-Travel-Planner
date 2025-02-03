from django.contrib.auth.views import LoginView
from django.urls import path
from users.forms import EmailOrUsernameAuthenticationForm

urlpatterns = [
    path('auth', LoginView.as_view(
        authentication_form=EmailOrUsernameAuthenticationForm
    ), name='login'),
]