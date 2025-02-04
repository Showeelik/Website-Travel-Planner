from celery import shared_task
from .models import Notification

@shared_task
def send_notification(user_id, message):
    """
    Создает уведомление для пользователя.
    """
    from django.contrib.auth import get_user_model
    User = get_user_model()

    try:
        user = User.objects.get(id=user_id)
        Notification.objects.create(user=user, message=message)
    except User.DoesNotExist:
        pass