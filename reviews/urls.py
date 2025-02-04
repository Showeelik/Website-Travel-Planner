from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('<int:route_id>/reviews', ReviewListCreateView.as_view(), name='review-list-create'),
    path('<int:route_id>/reviews/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
]