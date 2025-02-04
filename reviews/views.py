from rest_framework import generics, permissions
from django.db import IntegrityError
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

        try:
            serializer.save(user=user, route_id=route_id)
        except IntegrityError:
            raise ValidationError("Вы уже оставили отзыв на этот маршрут.")


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Получить, обновить или удалить отзыв.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)