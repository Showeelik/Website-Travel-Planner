from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameAuthBackend(BaseBackend):
    """
    Пользовательский бэкэнд аутентификации, позволяющий пользователям входить в систему, 
    используя либо имя пользователя или электронную почту.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Проверяем, является ли username email-адресом
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            # Находим пользователя по email или username
            user = UserModel.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None