from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .forms import EmailOrUsernameAuthenticationForm
from .views import home, register

urlpatterns = [
    path('', home, name='home'),
    path('auth', LoginView.as_view(
        authentication_form=EmailOrUsernameAuthenticationForm
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
]