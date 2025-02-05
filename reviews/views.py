from rest_framework import generics, permissions
from django.db import IntegrityError

from routes.models import Route
from notifications.tasks import send_notification
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.exceptions import ValidationError

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        route_id = self.kwargs['route_id']
        return Review.objects.filter(route_id=route_id)

    def perform_create(self, serializer):
        route_id = self.kwargs['route_id']
        user = self.request.user
        route = Route.objects.get(id=route_id)

        try:
            serializer.save(user=user, route_id=route_id)
        except IntegrityError:
            raise ValidationError("Вы уже оставили отзыв на этот маршрут.")

        # Отправляем уведомление владельцу маршрута
        if route.user != user:  # Не отправлять уведомление самому себе
            send_notification(route.user.id, f"Новый отзыв на ваш маршрут: {route.title}")
            
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Получить, обновить или удалить отзыв.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)