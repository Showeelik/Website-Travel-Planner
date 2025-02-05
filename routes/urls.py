from django.urls import path
from routes.views import RouteListView, RouteCreateView, RouteDetailView

urlpatterns = [
    path('routes', RouteListView.as_view(), name='route_list'),
    path('routes/create', RouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>', RouteDetailView.as_view(), name='route_detail'),
]