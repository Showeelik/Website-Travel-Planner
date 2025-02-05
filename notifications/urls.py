from django.urls import path
from notifications.views import notification_list

urlpatterns = [
    path('notifications', notification_list, name='notification_list'),
]