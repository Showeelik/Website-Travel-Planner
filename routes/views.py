from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from notifications.tasks import send_notification
from .models import Route
from reviews.forms import ReviewForm
from .forms import RouteForm

class RouteListView(LoginRequiredMixin, ListView):
    """
    Страница со списком маршрутов пользователя.
    """
    model = Route
    template_name = 'routes/route_list.html'
    context_object_name = 'routes'

    def get_queryset(self):
        # Показываем только маршруты текущего пользователя
        return Route.objects.filter(user=self.request.user)

class RouteCreateView(LoginRequiredMixin, CreateView):
    """
    Страница для создания нового маршрута.
    """
    model = Route
    form_class = RouteForm
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')  # Перенаправление после успешного создания

    def form_valid(self, form):
        # Привязываем маршрут к текущему пользователю
        form.instance.user = self.request.user
        return super().form_valid(form)


class RouteDetailView(LoginRequiredMixin, DetailView):
    """
    Страница с деталями маршрута и формой для создания отзыва.
    """
    model = Route
    template_name = 'routes/route_detail.html'
    context_object_name = 'route'

    def get_context_data(self, **kwargs):
        # Добавляем форму отзыва и список отзывов в контекст
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        # Обработка POST-запроса для создания отзыва
        self.object = self.get_object()
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.route = self.object

            try:
                review.save()

                # Отправляем уведомление владельцу маршрута
                if self.object.user != request.user:
                    send_notification(self.object.user.id, f"Новый отзыв на ваш маршрут: {self.object.title}")

                messages.success(request, "Отзыв успешно добавлен!")
                return redirect('route_detail', pk=self.object.pk)
            except IntegrityError:
                messages.error(request, "Вы уже оставили отзыв на этот маршрут.")

        # Если форма невалидна, рендерим страницу с ошибками
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)