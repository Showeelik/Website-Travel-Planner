from django.db import models
from users.models import User

class Location(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    latitude = models.FloatField(verbose_name='Широта',)
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.name

class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routes', verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Бюджет')
    duration = models.IntegerField(help_text="Duration in days", verbose_name='Длительность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    locations = models.ManyToManyField(Location, through='RouteLocation', verbose_name='Места')

    def __str__(self):
        return self.title

class RouteLocation(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='locations', verbose_name='Маршрут')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Место')
    order = models.PositiveIntegerField(verbose_name='Порядковый номер')

    class Meta:
        ordering = ['order']