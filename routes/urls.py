from django.urls import path
from routes import views

urlpatterns = [
    path('routes', views.route_list, name='route_list'),
    path('routes/create', views.route_create, name='route_create'),
    path('routes/<int:pk>', views.route_detail, name='route_detail'),
]