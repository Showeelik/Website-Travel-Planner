from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    """
    Custom authentication form to allow login with either username or email.
    """

    def clean_username(self):
        username = self.cleaned_data.get('username')
        UserModel = get_user_model()

        # Если введенный текст содержит '@', считаем его email
        if '@' in username:
            try:
                user = UserModel.objects.get(email=username)
                return user.username  # Возвращаем username для аутентификации
            except UserModel.DoesNotExist:
                pass

        return username  # Возвращаем оригинальное значение
    

class CustomUserCreationForm(UserCreationForm):
    """
    Custom form for user registration.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже используется.")
        return email