from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

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