from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для настройки Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_planner.settings')

app = Celery('travel_planner')

# Используйте Redis в качестве брокера
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически загружайте задачи из приложений Django
app.autodiscover_tasks()