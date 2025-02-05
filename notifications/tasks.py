from celery import shared_task
from .models import Notification
from django.contrib.auth import get_user_model

@shared_task
def send_notification(user_id, message):
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
        Notification.objects.create(user=user, message=message)
    except User.DoesNotExist:
        pass